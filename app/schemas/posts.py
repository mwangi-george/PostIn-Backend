from datetime import datetime

from pydantic import BaseModel


class PostCreate(BaseModel):
    content: str | None

    class Config:
        from_attributes = True


