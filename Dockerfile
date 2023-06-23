FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

WORKDIR /app


RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ADD . /app

COPY . /app

COPY ./entrypoint.sh /app/entrypoint.sh

ENTRYPOINT [ "sh" , "/app/entrypoint.sh" ]


