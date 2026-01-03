import pytest
from app import app
from db.database import SessionLocal
from db.models import User
from werkzeug.security import generate_password_hash

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "test-secret"
    app.config["WTF_CSRF_ENABLED"] = False

    with app.test_client as client:
        yield client