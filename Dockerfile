FROM python:3.7-slim-buster
LABEL maintainer="Huang Kai"

RUN sed -i "s@http://deb.debian.org@http://mirrors.tuna.tsinghua.edu.cn@g" /etc/apt/sources.list
RUN sed -i 's|security.debian.org/debian-security|mirrors.tuna.tsinghua.edu.cn/debian-security|g' /etc/apt/sources.list
RUN apt update
RUN apt install -y curl gcc default-libmysqlclient-dev

WORKDIR app
COPY requirements requirements
RUN pip install --upgrade pip \
    && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements/development.txt
COPY . .
