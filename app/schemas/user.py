from pydantic import BaseModel, EmailStr, Field


class ActionConfirm(BaseModel):
    msg: str | None


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., max_length=16, min_length=4)
    first_name: str
    last_name: str
    username: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "email": "user@gmail.com",
                "password": "1234",
                "first_name": "user",
                "last_name": "user",
                "username": "user"
            }
        }


class User(BaseModel):
    email: EmailStr
    username: str
    first_name: str
    last_name: str


class Token(BaseModel):
    access_token: str
    token_type: str
