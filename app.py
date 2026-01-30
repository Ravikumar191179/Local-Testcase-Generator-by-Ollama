from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from tools.generate_test_case import generate_test_case
import os

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    user_context = data.get('user_context')
    template_type = data.get('template_type', 'unit')
    
    if not user_context:
        return jsonify({"status": "error", "error_message": "No user_context provided"}), 400
        
    result = generate_test_case(user_context, template_type)
    return jsonify(result)

if __name__ == '__main__':
    print("🚀 Starting Testcase Generator on http://localhost:5001")
    app.run(host='0.0.0.0', port=5001, debug=True)
