from flask import Flask, render_template, request, url_for
import app.server as server

app = Flask(__name__)


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