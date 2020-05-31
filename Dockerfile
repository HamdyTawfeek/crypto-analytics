FROM python:3

WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
ADD . /usr/src/app
EXPOSE 8000