import json
from functools import wraps
from flask import request, abort, Flask, render_template, request, url_for
import app.server as server

app = Flask(__name__)


def require_api_key(view_function):
    """
    Decorator to enforce API key validation on Flask view functions.

    This decorator loads the list of valid API keys from a specified JSON file.
    
    It then checks the incoming request for an 'X-Api-Key' header and validates
    the provided API key against the list of keys loaded from the file.
    
    If the API key is valid, the request is allowed to proceed to 
    the decorated view function. If the API key is invalid or missing,
    an HTTP 401 Unauthorized error is returned.

    Args:
        view_function (function): The Flask view function to be decorated.

    Returns:
        function: The decorated view function which includes API key validation.

    Raises:
        FileNotFoundError: If the API keys file does not exist.
            with HTTP 500 Internal Server Error
        json.JSONDecodeError: If there is an error parsing the API keys file.
            with HTTP 500 Internal Server Error
        HTTP 401 Unauthorized if the API key is invalid or missing
    """
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        # Load API keys
        try:
            with open('app/credentials/api_keys.jsonk', 'r') as file:
                api_keys_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            abort(500, f'Error loading or parsing API keys file: {e}')

        # Retrieve the API key from the request header
        provided_api_key = request.headers.get('X-Api-Key')

        # Check if the provided API key matches any key in the file
        for item in api_keys_data.values():
            if provided_api_key == item.get('key'):
                return view_function(*args, **kwargs)

        # If no matching key is found, return an unauthorized error
        abort(401)  # Unauthorized access
    return decorated_function


@app.route('/', methods=['GET'])
def root_get():
    """The default GET view for hitting the application with a browser

    :return: the rendered template to the browser 
    """
    returned_data = 'Default Data'
    return render_template('main.html', data=returned_data)


@app.route('/', methods=['POST'])
def root_post():
    """The POST view for the default page. Requires form submitted data.
    Submitted data is passed to the "back-end" and reversed.
    Returned data is given to the rendered template.

    :return: the rendered template with returned data to the browser.
    """
    data = request.form['data']
    returned_data = server.submit_data(data)
    return render_template('main.html', data=returned_data)


@app.route('/api', methods=['GET'])
def api_get() -> dict:
    """The GET method page for the API view.

    :return: a default dict to indicate the API is working. 
    """
    returned_data = 'Default Data'
    status = 'Default'
    return {"status": status, "data": returned_data}


@app.route('/api', methods=['POST'])
@require_api_key
def api_post() -> dict:
    """The POST view for the API. Submitted data is passed to the "back-end"
    and "reversed". Returned data is given to the rendered template.

    :return: a dict with either error data or returned data
    """
    if 'data' in request.form:
        data = request.form['data']
        returned_data = server.submit_data(data)
        status = 'Success'
    else:
        returned_data = 'Error - No Data Submitted'
        status = 'Error'
    return {"status": status, "data": returned_data}


if __name__ == "__main__":
    app.run(debug=True)