FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY req.txt /code
RUN pip install --upgrade pip
RUN pip install -r /code/req.txt
RUN pip install psycopg2-binary

COPY . /code

EXPOSE 9000
