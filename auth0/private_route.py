from flask import Flask, jsonify
from authlib.integrations.flask_oauth2 import ResourceProtector

require_auth = ResourceProtector()

app = Flask(__name__)


@app.route("/api/private-scoped")
@require_auth(None)
def private_scoped():
    """A valid access token and scope are required."""
    response = (
        "Hello from a private endpoint! You need to be"
        " authenticated and have a scope of read:messages to see"
        " this."
    )
    return jsonify(message=response)
