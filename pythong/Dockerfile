FROM python:2.7-stretch

RUN apt update && apt -y upgrade

RUN mkdir /thot
WORKDIR /thot

RUN pip install rethinkdb==2.3.0.post6
COPY code.py ./code.py
COPY rrv.py ./rrv.py

CMD cd /thot && python code.py
