import firebase_admin
from firebase_admin import credentials
from firebase_admin import app_check
import flask
import jwt
import os

cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_PATH")  
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

flask_app = flask.Flask(__name__)

@flask_app.before_request
def verify_app_check() -> None:
    app_check_token = flask.request.headers.get("X-Firebase-AppCheck", default="")
    try:
        app_check_claims = app_check.verify_token(app_check_token)
        # If verify_token() succeeds, okay to continue to route handler.
    except (ValueError, jwt.exceptions.DecodeError):
        flask.abort(401)    

@flask_app.route("/")
def hello_world():
    return "<p>Hello, World!!</p>"


# El inicializador debe ir hast aca, si no no detecta la ruta 
if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=5001, debug=True)

