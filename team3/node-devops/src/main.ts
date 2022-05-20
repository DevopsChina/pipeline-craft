import { NestFactory } from '@nestjs/core';
import { NestExpressApplication } from '@nestjs/platform-express';
import { join } from 'path';
import { AppModule } from './app.module';
import * as apm from 'elastic-apm-node';

const envdata = process.env.env;

const apmClient = apm.start({
  serviceName: envdata === 'prod' ? 'node' : 'node-dev',
  secretToken: 'mwZPM5XBD7qULjw9J1',
  serverUrl:
    'https://cfa9161c5a774bd4934ad2f63e43c02f.apm.us-central1.gcp.cloud.es.io:443',
  environment: envdata === 'prod' ? 'production' : 'dev',
});

async function bootstrap() {
  const app = await NestFactory.create<NestExpressApplication>(AppModule);
  app.setViewEngine('pug');
  app.setBaseViewsDir(join(__dirname, '..', 'views'));
  app.useStaticAssets(join(__dirname, '..', 'public'));

  await app.listen(80);
}
bootstrap();
