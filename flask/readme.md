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
        |---static/        <--- directory for static front-end resources, like CSS files
        |---templates/     <--- directory for HTML code
        |---work_files/    <--- optional directory for writing out or reading in data
        |---credentials/   <--- credentials for accessing the app, when required
    |---tests/             <--- directory containing all Python tests (see "tests" below)
        |---coverage       <--- directory containing coverage.py resources
            .coveragerc    <--- the configuration file for coverage.py
    Dockerfile             <--- contains all the commands to build the Flask container
    requirements_flask.txt <--- requirements file for starting flask application
    requirements.txt       <--- requirements for use with a virtual environment, for testing etc
    readme.md              <--- this file
```

## API Keys File (`api_keys.jsonk`)

### Overview

The `api_keys.jsonk` file is used to store API keys for authenticating requests to selected endpoints of the application. Each key is associated with a comment explaining its purpose or the application it is intended for. This file should be placed in the `credentials` directory at the root of the app.

### Format

The file contains a JSON object where each entry consists of a numeric string as a key, and the value is another object with two properties: `key` and `comment`. The `key` property holds the actual API key, while the `comment` property provides a description or note about the key.

### Example

```json
{
    "0": {
        "key": "MyAPIKey1",
        "comment": "This key is for Application A"
    },
    "1": {
        "key": "AnotherAPIKey",
        "comment": "This key is for Application B"
    }
}
```

### Usage

The application reads this file to authenticate API requests. When making a request, include the API key in the X-Api-Key request header. The server will verify the API key against those listed in the api_keys.jsonk file.

### Security

- DO NOT commit this file to version control.
- Ensure api_keys.jsonk is listed in your .gitignore file to prevent accidental exposure of API keys.
- Regularly rotate and review API keys to ensure they remain secure.
- Future: transition to a more secure key management system for production environments.

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

#### GET method
``` curl -X GET http://localhost:8080/api```

#### POST method with API Key
```curl -X POST -H "X-Api-Key: YourActualAPIKeyHere" -d "data=reverse me" http://localhost:8080/api```

