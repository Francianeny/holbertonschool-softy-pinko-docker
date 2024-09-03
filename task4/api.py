# api.py for task4
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from task4 backend!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)
