# Flask Docker Lab

Simple Docker practice project with a Flask application and PostgreSQL.

![Pipeline Stages](images/docker-flask-postgresql2.png)

## Technologies

- Python
- Flask
- Docker
- Docker Compose
- PostgreSQL

## Actions

- Building Docker images
- Running containers
- Port mapping
- Using Docker Compose
- Connecting a Flask application to PostgreSQL
- Inspecting containers and checking logs

## Run the project

```bash
docker compose up --build
```

## Checking logs
```
docker logs humble-frog
docker inspect humble-frog
```

## Enter the container

```
docker exec -it humble-frog /bin/sh
```