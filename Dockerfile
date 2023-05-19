FROM python:slim

RUN useradd khg

WORKDIR /home/go-khg

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql cryptography

COPY app app
COPY go-khg.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP go-khg.py

RUN chown -R khg:khg ./
USER khg

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]