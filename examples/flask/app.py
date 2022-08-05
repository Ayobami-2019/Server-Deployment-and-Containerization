from flask import Flask
APP = Flask(__name__)


@APP.route('/')
def hello_world():
    return 'Hello, World from Flask!\n'

# GET '/': This is a simple health check, which returns the response 'Healthy'.
# POST '/auth': This takes an email and password as json arguments and returns a JWT based on a custom secret.
# GET '/contents': This requires a valid JWT, and returns the decrypted contents of that token.

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
