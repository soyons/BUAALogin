FROM python:3.7.12-alpine

COPY . /app/

WORKDIR /app

RUN pip install -r /app/requirements.txt

ENTRYPOINT ["python","-u","always_online.py"]
