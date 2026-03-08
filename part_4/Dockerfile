FROM python:3.12-slim

WORKDIR /app

COPY ./part_4/requirements.txt .

RUN pip install -r requirements.txt

COPY ./part_4 .

CMD [ "python" , "main.py" ]