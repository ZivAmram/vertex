FROM python:3.9

WORKDIR /app

COPY main.py /app
COPY logs /app/logs

RUN pip3 install pytz

CMD ["python", "/app/main.py"]

