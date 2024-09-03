from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Example endpoint
@app.route('/api/data', methods=['GET'])
def get_data():
    # Placeholder data; replace with actual data handling as needed
    data = {
        'message': 'Hello from Task 5 API!',
        'task': 5
    }
    return jsonify(data)

# Additional endpoints can be defined here as required
@app.route('/api/info', methods=['GET'])
def get_info():
    info = {
        'info': 'This is task 5 additional info endpoint',
        'version': '1.0'
    }
    return jsonify(info)

# Endpoint to handle POST requests
@app.route('/api/submit', methods=['POST'])
def submit_data():
    submitted_data = request.json
    # Processing logic goes here
    response = {
        'status': 'success',
        'received': submitted_data
    }
    return jsonify(response)

if __name__ == '__main__':
    # Set the host to 0.0.0.0 to make the service accessible from outside the container
    app.run(host='0.0.0.0', port=5252)
