# Flask Nginx Container

This repository contains all the files required to create a fully operational, two container (flask and nginx) web application.

The application uses:

- Python 3.11
- Gunicorn WSGI
- Flask front-end
- Nginx Web Server
- Docker (or any container run-time)

## Subdirectories and Files

- nginx: files needed to start the nginx container
- flask: files for starting the flask container, modifying the flask_application, and testing Python code
- docker-compose.yml: Docker compose file for bringing up both containers and starting the application

__( more flask detail in flask/readme.md)__

## docker reference commands

### list containers

```
sudo docker container ls
```

### Bring up container environment with docker-compose yaml file

```
sudo docker-compose up --build -d
```

#### Stop containers and remove them, if needed

```
sudo docker stop nginx
sudo docker rm nginx
sudo docker stop flask
sudo docker rm flask
```

### Accessing application logs inside the containers

```
sudo docker logs flask
sudo docker logs nginx
```
