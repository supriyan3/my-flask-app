from flask import Flask, jsonify
import os

app = Flask(__name__)

# Config via environment variables
APP_NAME = os.getenv('APP_NAME', 'MyFlaskApp')
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')

@app.route('/')
def home():
    return jsonify({
        'name': APP_NAME,
        'version': APP_VERSION,
        'message': 'Hello from Flask!'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
