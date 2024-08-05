from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas import UserCreate, ActionConfirm, Token
from app.services import UserServices
from app.utilities import get_db, RateLimiter

rate_limiter = RateLimiter()


def create_user_routes() -> APIRouter:
    router = APIRouter(
        prefix="/users",
        tags=["users"],
        dependencies=[Depends(rate_limiter.rate_limit)]
    )

    user_services = UserServices()

    @router.post('/new', response_model=ActionConfirm, status_code=status.HTTP_201_CREATED)
    async def create_user(user_profile: UserCreate, db: Session = Depends(get_db)):
        msg = user_services.create_user(user_profile, db)
        formatted_msg = ActionConfirm(msg=msg)
        return formatted_msg

    @router.post('/login', response_model=Token, status_code=status.HTTP_200_OK)
    async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
        token = user_services.login_user(form_data.username, form_data.password, db)
        return token

    return router
