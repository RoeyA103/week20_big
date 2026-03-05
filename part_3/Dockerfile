FROM python:3.12-slim

WORKDIR /app

COPY ./part_3/requirements.txt .

RUN pip install -r requirements.txt

COPY ./part_3 .

CMD [ "python" , "main.py" ]