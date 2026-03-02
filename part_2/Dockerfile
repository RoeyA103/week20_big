FROM python:3.11-slim

WORKDIR /app

COPY ./part_2/requirements.txt .

RUN pip install -r requirements.txt

COPY ./part_2 .

CMD [ "python" , "main.py" ]