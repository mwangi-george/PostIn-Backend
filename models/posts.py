from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from datetime import datetime, timezone

from .base import Base


class Posts(Base):
    __tablename__ = 'posts'

    post_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False
    )
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False, index=True)
