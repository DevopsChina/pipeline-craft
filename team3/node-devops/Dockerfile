FROM harbor.devops.soulchild.cn/devops/node:12

WORKDIR /usr/src

COPY . .

EXPOSE 80

CMD node --max-http-header-size=16384 dist/main
