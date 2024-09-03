from flask import Flask

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return "Hello from Task 1"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)
