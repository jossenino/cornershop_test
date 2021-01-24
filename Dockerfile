FROM python:3.7 

ENV PYTHONUNBUFFERED=1 

RUN mkdir /code 
RUN mkdir /data 

WORKDIR /code 

COPY django-version.txt /code/ 

RUN pip install -r django-version.txt 

RUN pip install slack_sdk

COPY . /code/