FROM ubuntu:latest

COPY . /app
WORKDIR /app

ENV PORT 8080
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update \
    && apt-get install -y python3 \
    && apt-get install -y python3-pip \
    && python3 -m pip install --upgrade pip \
    && pip3 install --no-cache-dir --upgrade -r requirements.txt

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8080"]
