FROM python:3.8.13-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /django_test

COPY . .

RUN pip install -r requirements.txt

RUN python manage.py migrate

RUN python manage.py runscript set_admins

EXPOSE 8000