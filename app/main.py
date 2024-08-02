# This is the main entry point of the application

from fastapi import FastAPI
from app.routes import user_routes, posts_routes


def create_app() -> FastAPI:
    server = FastAPI()

    user_router = user_routes()
    posts_router = posts_routes()
    server.include_router(user_router)
    server.include_router(posts_router)
    return server


# start app
app = create_app()
