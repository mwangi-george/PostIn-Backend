from fastapi import APIRouter, Depends, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services import PostServices
from app.schemas import PostCreate, ActionConfirm
from app.utilities import Security, get_db
from models import User

security = Security()


def create_posts_routes() -> APIRouter:
    router = APIRouter(
        prefix="/posts",
        tags=["posts"]
    )
    post_services = PostServices()

    @router.post('/new', response_model=ActionConfirm, status_code=status.HTTP_201_CREATED)
    async def create_post(
            post_details: PostCreate,
            db: Session = Depends(get_db),
            current_user: User = Depends(security.get_current_user)
    ):
        user_id = current_user.user_id
        post_id = post_services.create_post(post=post_details, user_id=user_id, db=db)
        msg = f"Post with id {post_id} created successfully."
        formatted_msg = ActionConfirm(msg=msg)
        return formatted_msg

    @router.put('/update_post/{post_id}/', response_model=ActionConfirm, status_code=status.HTTP_200_OK)
    async def update_post(
            post_id: int,
            post_details: PostCreate,
            db: Session = Depends(get_db),
            current_user: User = Depends(security.get_current_user)
    ):
        post_id = post_services.update_post(post_id=post_id, post=post_details, db=db)
        msg = f"Post with id {post_id} updated successfully."
        formatted_msg = ActionConfirm(msg=msg)
        return formatted_msg

    @router.delete('/delete_post/{post_id}/', status_code=status.HTTP_200_OK)
    async def delete_post(post_id: int):
        pass

    @router.get('/get_posts/{post_id}/{user_id}', status_code=status.HTTP_200_OK)
    async def get_post(post_id: int, current_user: User = Depends(security.get_current_user)):
        pass

    @router.get('/get_posts/all/{user_id}', status_code=status.HTTP_200_OK)
    async def get_posts():
        pass

    return router
