FROM python:3.9.7-slim

ADD . /opt/c2c

WORKDIR /opt/c2c

RUN pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple && pip install pyyaml
