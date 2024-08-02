from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, ActionConfirm, Token, User
from app.services.user import UserServices, security
from app.utilities import get_db


def create_user_routes() -> APIRouter:
    router = APIRouter(
        prefix="/users",
        tags=["users"],
    )

    user_services = UserServices()

    @router.post('/user', response_model=ActionConfirm, status_code=status.HTTP_201_CREATED)
    async def create_user(user_profile: UserCreate, db: Session = Depends(get_db)):
        msg = user_services.create_user(user_profile, db)
        formatted_msg = ActionConfirm(msg=msg)
        return formatted_msg

    @router.post('/login', status_code=status.HTTP_200_OK)
    async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
        token = user_services.login_user(form_data.username, form_data.password, db)
        # formatted_token = Token(**token)
        return token

    return router
