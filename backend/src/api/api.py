from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.users_router import user_router

app = FastAPI(
    title="Let me save money",
    description="API for let me save money app",
    version="0.1.0"
)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
