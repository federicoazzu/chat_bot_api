from flask import Flask, request
from collections import namedtuple

app = Flask(__name__)


#  Your home page
@app.route('/')
def index():
    return f'<h1>Home Page</h1>'


#  Create an api endpoint where you can query
@app.route('/api')
def api():
    user_input = request.args.get('input')
    response = generate_response(user_input)

    json = {
        'input': user_input,
        'response': response.response,
        'accuracy': response.accuracy
    }

    return json


# Convenience tuple for returning responses
Response = namedtuple('Response', 'response accuracy')


#  Create the functionality that you want.
def generate_response(user_input: str) -> Response:
    lc_input = user_input.lower()

    if lc_input == "hello":
        return Response("Hey there!", 1)
    elif lc_input == "goodbye":
        return Response("See you later!", 1)
    else:
        return Response("Could not understand.", 0)


if __name__ == '__main__':
    app.run()
