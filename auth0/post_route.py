from flask import Flask, jsonify, request
from authlib.integrations.flask_oauth2 import ResourceProtector

require_auth = ResourceProtector()

app = Flask(__name__)



@require_auth(None)
@app.route("/api/stablediff/generate", methods=["POST"])
def private_scoped():
    data = request.get_json()
    if 'description' not in data:
        return jsonify(message="description is required"), 400
    description = data['description']
    return jsonify(message="success")