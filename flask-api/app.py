from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health')
def health_check():
    return 'OK', 200

@app.route('/environment')
def environment():
    environment = os.environ.get('FLASK_ENVIRONMENT', 'unknown')
    return jsonify({'environment': environment})

if __name__ == '__main__':
    app.run(port=5050)