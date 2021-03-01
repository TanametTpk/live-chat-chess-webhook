from flask import Flask, request, jsonify, render_template
from chess import move

app = Flask(__name__)

@app.route('/webhooks', methods=["POST"])
def webhooks():
    contents = request.json
    for content in contents:
        if "message" in content:
            move(content["message"])
    return jsonify({"status": 200})

@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)