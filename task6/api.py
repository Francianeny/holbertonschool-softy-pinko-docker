from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Activer CORS pour toutes les routes

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify('Hello from Task 6')

@app.route('/data', methods=['GET'])
def get_data():
    # Exemple de point de terminaison pour renvoyer des données
    data = {
        "id": 1,
        "name": "Softy Pinko Task 6",
        "description": "Sample data for task 6"
    }
    return jsonify(data)

@app.route('/echo', methods=['POST'])
def echo():
    # Exemple de point de terminaison pour renvoyer les données reçues
    data = request.json
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5252)
