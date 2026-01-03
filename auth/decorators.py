# ...existing code...
from functools import wraps
from flask import session, jsonify
import logging

logger = logging.getLogger(__name__)

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            logger.warning("Unauthorized access attempt")
            return jsonify({"error": "Unauthorized"}), 401
        return func(*args, **kwargs)
    return wrapper

def role_required(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if "user_id" not in session:
                logger.warning("Unauthorized access attempt")
                return jsonify({"error": "Unauthorized"}), 401
            if session.get("role") != required_role:
                logger.warning("Unauthorized access attempt")
                return jsonify({"error": "Forbidden"}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator
# ...existing code...