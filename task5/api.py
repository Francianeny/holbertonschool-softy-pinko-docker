from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify('Hello from Task 5')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)
