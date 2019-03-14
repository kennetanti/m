FROM python:3.7-stretch

RUN apt update && apt -y upgrade

RUN mkdir /thot
WORKDIR /thot

RUN pip install rethinkdb
COPY code.py ./code.py
COPY rrv.py ./rrv.py

CMD cd /thot && python code.py
