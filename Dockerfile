FROM python:3.7-slim-stretch
LABEL maintainer="Huang Kai"

WORKDIR app
COPY requirements requirements
RUN pip install --upgrade pip \
    && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements/development.txt

