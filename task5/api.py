from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Exemple de données à retourner
    data = {
        "message": "Hello from Task 5 API!",
        "task": 5
        }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)
