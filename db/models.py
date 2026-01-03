from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = "users"  # table name "users" in a single "User" class

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default="user")

#-------------------------------------------------------------------------------#

# Base → base class for all DB tables
# User → represents users table
# Each attribute → one column
# SQLAlchemy converts this into SQL automatically
# This is called ORM (Object Relational Mapping).