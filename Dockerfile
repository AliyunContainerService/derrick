FROM python:2.7-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD . /app

CMD ["python"]