from fastapi import APIRouter
from app.routers import users, items
from .military import router as military_router

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(military_router, prefix="/military", tags=["military"])

# IDE가 인식할 수 있도록 명시적으로 import
__all__ = ["api_router", "users", "items"]
