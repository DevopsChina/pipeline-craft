import { AppService } from './app.service';
import { Response } from 'express';
import { Controller, Get, Query, Res } from '@nestjs/common';

const envdata = process.env.env;

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get('/')
  async index(@Query() query, @Res() res: Response) {
    try {
      const data = await this.appService.getHello();
      res.header('Http-X-Requestid', data.request_id);
      return res.render('index', { data: JSON.stringify(data), envdata });
    } catch {
      return res.render('index', {
        data: '获取失败',
        envdata,
      });
    }
  }

  @Get('/health')
  async health(@Query() query, @Res() res: Response) {
    return res.send({ healthy: true });
  }
}
