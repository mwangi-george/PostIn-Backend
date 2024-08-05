from fastapi import FastAPI, Depends
from app.routes import user_routes, posts_routes


def create_app() -> FastAPI:
    """Main Application Entry Point """
    server = FastAPI(
        title="PostIn API service for users and posts management",
        description="Developed with ❤️ by [George Mwangi](https://github.com/mwangi-george)."
                    " [Source Code](https://github.com/mwangi-george/PostIn)",
        version="1.0.1"
    )

    user_router = user_routes()
    posts_router = posts_routes()
    server.include_router(user_router)
    server.include_router(posts_router)
    return server


app = create_app()
