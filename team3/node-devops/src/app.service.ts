import { Injectable } from '@nestjs/common';
import axios from 'axios';
import { v4 as uuidv4 } from 'uuid';

const envdata = process.env.env;

axios.interceptors.request.use((request) => {
  console.log(
    JSON.stringify({
      text: `${request.method} ${request.url}`,
      record: {
        extra: {
          service_name: 'node',
          request_id: request.headers['Http-X-Requestid'],
        },
      },
    }),
  );
  return request;
});

@Injectable()
export class AppService {
  async getHello(): Promise<any> {
    const uuid = uuidv4();
    const { data } = await axios.get(
      `http://python${
        envdata === 'prod' ? '' : '-test'
      }.devops.soulchild.cn/api/a`,
      {
        headers: {
          'Http-X-Requestid': uuid,
        },
      },
    );
    return { ...data, request_id: uuid };
  }
}
