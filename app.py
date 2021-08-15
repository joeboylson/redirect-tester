import os
import json

from flask import Flask, request

app = Flask(__name__)

IS_PRODUCTION = os.environ.get('PYTHON_ENV') == 'PRODUCTION'
DEBUG = True if not IS_PRODUCTION else False
PORT = 5000 if not IS_PRODUCTION else os.environ.get('PORT')

@app.route("/", defaults={"path": ""})
@app.route("/<string:path>")
@app.route("/<path:path>")
def index(path):

    return json.dumps({
        "path": path,
        "args": request.args
    })

if __name__ == '__main__':
    print('::: {}'.format(PORT))
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
