
from flask import Flask, jsonify
from authlib.integrations.flask_oauth2 import ResourceProtector
from auth0.TokenValidator import Auth0JWTBearerTokenValidator

require_auth = ResourceProtector()
domain = getenv('AUTH0_DOMAIN')
api_identifier = getenv('AUTH0_ALLOWED_ORIGINS')
validator = Auth0JWTBearerTokenValidator(
    f"{domain}",
    f"{api_identifier}"
)
require_auth.register_token_validator(validator)

app = Flask(__name__)

