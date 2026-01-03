from flask import Blueprint, request, session, jsonify
from utils.security import hash_password,verify_password
from db.models import User
# from db.database import SessionLocal
from utils.db_session import get_db
from .decorators import login_required, role_required
import logging

logger = logging.getLogger(__name__)

auth_bp = Blueprint("auth",__name__)

@auth_bp.route("/login", methods = ["POST"])
def login():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    logger.info(f"Login attempt for user: {username}")

    db = get_db()
    user = db.query(User).filter(User.username == username).first()   # or (User.username == username)
    db.close()

    if not user or not verify_password(password, user.password_hash):
        logger.warning(f"failed login attempt for user {username}")
        return {"message": "Invalid credentials"}, 401

    session["user_id"] = user.id
    session["role"] = user.role
    logger.info(f"user logged in successfully: {username}")

    return jsonify({"message": "Login successfully"}), 200


# register
@auth_bp.route("/register", methods = ["POST"])
def register():
    data = request.json
    
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"message": "Username and Password required"}, 400

    db = get_db()

    if db.query(User).filter(User.username == username).first():
        return {"message": "user already exists"}, 400

    new_user = User(
        username = username,
        password_hash = hash_password(password)
    )

    db.add(new_user)
    db.commit()
    db.close()

    return {"message": "user registered successfully"}, 201


# logout
# @auth_bp.route("/logout", methods = ["POST"])
# def logout():
#     session.clear()
#     response = jsonify({"message": "Logged out successfully"})
#     response.delete_cookie("session")
#     return response, 200

#logout
@auth_bp.route("/logout", methods=["POST"])
def logout():
    user_id = session.get("user_id")
    session.pop("user_id", None)   # or "username" (match login!)
    response = jsonify({"message": "Logged out successfully"})

    logger.info(f"user logged out: {user_id}")
    return response, 200


# dashboard
@auth_bp.route("/dashboard")
@login_required
def dashboard():
    return {"message": "welcome to dashboard"}



# admin route (no change)
@auth_bp.route("/admin")
@role_required("admin")
def admin_panel():
    return {"message": "Welcome Admin"}
