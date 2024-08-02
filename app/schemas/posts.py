from datetime import datetime

from pydantic import BaseModel


class PostCreate(BaseModel):
    content: str | None

    class Config:
        from_attributes = True


class Post(BaseModel):
    post_id: int
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "post_id": 1,
                "content": "We love fastapi",
                "created_at": "2020-08-02 13:24:46.281204",
                "updated_at": "2020-08-02 13:24:46.281204"
            }
        }


class ManyPosts(BaseModel):
    posts: list[Post] | None
