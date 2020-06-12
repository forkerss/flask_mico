FROM python:3.7
RUN mkdir /app
ADD . /app/

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ --no-cache-dir -r /app/requirements.txt

WORKDIR /app