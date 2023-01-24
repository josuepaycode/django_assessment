FROM python:3.11.1-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip setuptools wheel pipenv

# Copy code and dependencies
COPY ./Pipfile ./Pipfile.lock /app/
COPY ./django_test /app/django_test
WORKDIR /app/django_test

# Crete new container user
RUN adduser -D -g '' test && chown test:test -R /app
USER test

# Install dependecies
RUN pipenv sync

ENTRYPOINT ["pipenv", "run"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
