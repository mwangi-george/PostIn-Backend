from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import timedelta
from app.schemas.user import UserCreate
from models import User
from app.utilities.security import Security


security = Security()


class UserServices:
    """A class to handle user routes"""

    def __init__(self):
        pass

    @staticmethod
    def create_user(user_profile: UserCreate, db: Session):
        db_user_name = db.query(User).filter_by(username=user_profile.username).first()
        db_user_email = db.query(User).filter_by(email=user_profile.email).first()

        def registration_exception(what_to_check):
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=f"{what_to_check} is already taken!"
            )

        if db_user_name:
            return registration_exception(db_user_name.username)

        if db_user_email:
            return registration_exception(db_user_email.email)

        user = User(
            email=user_profile.email,
            username=user_profile.username,
            password=security.get_password_hash(user_profile.password),
            first_name=user_profile.first_name,
            last_name=user_profile.last_name
        )

        try:
            db.add(user)
            db.commit()
            db.refresh(user)
            return "User created successfully"
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not create user"
            )

    @staticmethod
    def login_user(username, password, db: Session):
        user = security.authenticate_user(username, password, db)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
        access_token = security.create_access_token(data={"sub": user.username}, expires_in=timedelta(minutes=60))
        print(access_token)
        return {"access_token": access_token, "token_type": "bearer"}

