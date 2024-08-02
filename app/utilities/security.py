import os
from datetime import timedelta, datetime, timezone
from dotenv import load_dotenv

from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.utilities import get_db
from models import User


class Security:
    def __init__(self):
        load_dotenv()

    ACCESS_TOKEN_EXPIRE_MINUTES = 3
    ALGORITHM = os.environ.get("ALGORITHM")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, data, expires_in: timedelta | None = None):
        to_encode = data.copy()
        if expires_in:
            expire = datetime.now(timezone.utc) + expires_in
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.JWT_SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    def authenticate_user(self, username: str, password: str, db: Session):
        user = db.query(User).filter(User.username == username).first()
        if not user:
            return False
        if not self.verify_password(password, user.password):
            return False
        return user

    def get_current_user(self, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
        try:
            payload = jwt.decode(token, self.JWT_SECRET_KEY, algorithms=[self.ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = db.query(User).filter(User.username == username).first()
        if not user:
            raise credentials_exception
        return user
