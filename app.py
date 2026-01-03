from flask import Flask, render_template
from config_loader import config
from auth.routes import auth_bp
from db.database import init_db
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") or config["auth"]["secret_key"]

@app.route("/health")
def health():
    return {"status": "ok"}, 200

app.register_blueprint(auth_bp)

# app.config.update(
#     SESSION_PERMANENT = False,
#     SESSION_USE_SIGNER = True
# )

if __name__ == "__main__":
    logger.info("Starting Flask application")
    
    if os.getenv("APP_ENV", "dev") == "dev":
        init_db()

    app.run(
        port = config["server"]["port"],
        debug = config["server"]["debug"]
    )
    

