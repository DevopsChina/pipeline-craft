FROM harbor.devops.soulchild.cn/devops/python:3.8
COPY ./src /devops
COPY requirements.txt /
WORKDIR /devops
ENV ENV prod

# RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
CMD ["python3", "server.py"]








