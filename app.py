from flask import Flask, abort, request, redirect
import xiaoai_handler
from music_handler import *


app = Flask(__name__)


@app.route('/soundbox', methods=['POST'])
def handler():
    if not request.json:
        abort(400)
    response = xiaoai_handler.parse_input(request.json)
    return response


@app.route('/play', methods=['GET'])
def player():
    source = request.args.get('s')
    id = request.args.get('id')
    real_url = eval(f"{source}.play('{id}')")
    if real_url:
        return redirect(real_url)
    else:
        return abort(404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8007)
