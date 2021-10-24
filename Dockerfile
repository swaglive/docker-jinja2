FROM        python:3.10.0-alpine3.14

ENTRYPOINT  ["jinjacli"]

COPY        requirements.txt requirements.txt

RUN         pip install -r requirements.txt

COPY        jinjacli.py /usr/local/bin/jinjacli

RUN         chmod +x /usr/local/bin/jinjacli
