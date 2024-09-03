from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return jsonify({
        "message": "Hello from Task 3",
        "details": "This is a more detailed response"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)
