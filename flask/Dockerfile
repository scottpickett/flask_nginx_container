# syntax=docker/dockerfile:1

FROM python:3.11
WORKDIR /flask
COPY requirements.txt requirements_flask.txt
RUN pip3 install -r requirements_flask.txt
COPY . .

# CMD [ "python3", "-m" , "flask", "--app", "app.app", "run", "--host=0.0.0.0"]  # the old way of doing it without nginx

