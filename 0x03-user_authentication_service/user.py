from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User class to represent the users table in the database
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, max_length=250)
    hashed_password = Column(String, nullable=False, max_length=250)
    session_id = Column(String, max_length=250)
    reset_token = Column(String, max_length=250)
