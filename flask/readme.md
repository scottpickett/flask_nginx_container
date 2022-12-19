# Python Flask Generic Application

## Description

This is a simple and generic application intended as a Proof of Concept for:

- containerizing a fully functioning Python Flask application with the following features:
    - a web page with a submission form to demo GET and POST functionality
    - an API that:
        - displays a response (GET)
        - takes JSON data submission (POST)
    - a "back-end" application that reverses the string representation of the submitted data, and returns it to the "front-end".
    - pre-created test architecture for TDD

## Directories

```
flask/
    |---app/
            app.py         <--- the main applicaiton file with the Flask views ("front-end")
            server.py      <--- the "back-end" application file with application functions
            wsgi.py        <--- the web server callable WSGI Python file to launch the Flask app
    |---static/            <--- directory for static front-end resources, like CSS files
    |---templates/         <--- directory for HTML code
    |---work_files/        <--- optional directory for writing out or reading in data
    |---tests/             <--- directory containing all Python tests (see "tests" below)
        |---coverage       <--- directory containing coverage.py resources
            .coveragerc    <--- the configuration file for coverage.py
    Dockerfile             <--- contains all the commands to build the Flask container
    requirements_flask.txt <--- requirements file for starting flask application
    requirements.txt       <--- requirements for use with a virtual environment, for testing etc
    readme.md              <--- this file
```

## Tests

### Running unit tests

from ```flask/:```

```python3 -m pytest -r tests```

### Reviewing test coverage

from ```flask/:```

ASCII test coverage report:

```python3 -m pytest --cov-config=tests/coverage/.coveragerc --cov-branch --cov=app .```

HTML test coverage report:

```python3 -m pytest --cov-config=tests/coverage/.coveragerc --cov-report=html:tests/coverage/coverage_html --cov=app .```

### UI and API testing

## run gunicorn manually

```./venv/bin/gunicorn --log-level debug --access-logfile './logs/access-log' --error-logfile './logs/error-log' --reload --bind 127.0.0.1:5000 app.wsgi:app```

### web test

```curl -X GET localhost:8080/api```
```curl -X POST -d data="reverse me" server1:8080/api```
