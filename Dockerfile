# FROM python

# COPY . /app
# WORKDIR /app

# ENV PORT 8080
# ENV PYTHONUNBUFFERED=1
# ENV PYTHONDONTWRITEBYTECODE=1


# RUN python -m pip install --upgrade pip
# RUN pip install --no-cache-dir --upgrade -r requirements.txt

# CMD exec gunicorn core.wsgi:application --bind 0.0.0.0:8080

FROM python

COPY . /app
WORKDIR /app

ENV PORT 8080
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN python manage.py collectstatic --no-input

CMD exec gunicorn core.wsgi:application --bind 0.0.0.0:8080
