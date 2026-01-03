from db.database import SessionLocal
from db.models import User
from werkzeug.security import generate_password_hash

def create_user():
    db = SessionLocal()
    user = User(
        username = "nik",
        password_hash = generate_password_hash("pass123")
    )
    db.add(user)
    db.commit()
    db.close()
    print("user created successfully")

if __name__ == "__main__":
    create_user()
    
