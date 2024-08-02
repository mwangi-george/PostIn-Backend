from sqlalchemy import Column, Integer, String, Boolean

from .base import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False, index=True)
    last_name = Column(String, nullable=False, index=True)
    username = Column(String, nullable=False, unique=True, index=True)
    is_active = Column(Boolean, nullable=False, default=True)
