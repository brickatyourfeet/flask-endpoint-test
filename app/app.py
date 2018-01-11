from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'message': 'Nothing important'})



if __name__ == '__main__':
    app.run()