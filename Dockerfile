FROM python:slim

RUN useradd khg

WORKDIR /home/khg

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY go-khg.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP khg.py

RUN chown -R khg:khg ./
USER khg

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]