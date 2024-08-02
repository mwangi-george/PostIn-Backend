from datetime import datetime, timezone

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import User, Posts
from app.schemas import PostCreate


class PostServices:
    def __init__(self):
        pass

    @staticmethod
    def create_post(post: PostCreate, user_id: int, db: Session) -> int:
        db_post = Posts(
            content=post.content,
            created_at=datetime.now(timezone.utc),
            user_id=user_id
        )

        try:
            db.add(db_post)
            db.commit()
            db.refresh(db_post)
            return db_post.post_id
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    @staticmethod
    def update_post(post_id: int, post: PostCreate, db: Session) -> int:
        db_post = db.query(Posts).filter(Posts.post_id == post_id).first()
        if db_post is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Post with id {post_id} does not exist"
            )
        try:
            db_post.content = post.content
            db_post.updated_at = datetime.now(timezone.utc)
            db.commit()
            db.refresh(db_post)
            return db_post.post_id
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,

            )
