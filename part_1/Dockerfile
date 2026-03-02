FROM python:3.11-slim

WORKDIR /app

COPY ./part_1/requirements.txt .

RUN pip install -r requirements.txt

COPY ./part_1 .

CMD [ "python" , "main.py" ]