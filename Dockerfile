FROM python:3.10.0-alpine3.14

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /usr/src/app

COPY main.py main.py

CMD ["python3" , "main.py"]