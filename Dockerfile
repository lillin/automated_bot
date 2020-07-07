FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /opt/service
WORKDIR /opt/service
COPY requirements.txt /opt/service
RUN pip install -r requirements.txt
COPY . /opt/service