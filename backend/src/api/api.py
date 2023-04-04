from fastapi import FastAPI

from .routes.users_router import user_router

app = FastAPI(
    title="Let me save money",
    description="API for let me save money app",
    version="0.1.0"
)

app.include_router(user_router)
