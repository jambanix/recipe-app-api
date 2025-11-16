
# Recipe app API notes

## Project setup

1. Install docker and docker componse on PC
2. Create API key on docker hub
3. Add Docker Hub username and API key to repository secrets on Github

## Docker with Django

To run commands for Django inside the container:

```bash
docker-compose run --rm app sh -c "python manage.py collectstatic"
```

- Create Dockerfile
- Set up Dockerfile

```bash
FROM python:3.9-alpine3.13
LABEL maintainer="jambanix"
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"
USER django-user
```

- **Never use the root user, always create a user inside the container for running the app**
- To run the container:

```bash
docker build .
```

- Create docker-compose.yaml