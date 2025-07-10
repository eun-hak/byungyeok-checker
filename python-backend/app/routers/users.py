from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.user import User, UserCreate, UserUpdate
from app.services.user_service import UserService

router = APIRouter()

@router.get("/", response_model=List[User])
async def get_users():
    """모든 사용자 목록 조회"""
    return UserService.get_all_users()

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    """특정 사용자 조회"""
    user = UserService.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    """새 사용자 생성"""
    return UserService.create_user(user)

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate):
    """사용자 정보 업데이트"""
    updated_user = UserService.update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    """사용자 삭제"""
    success = UserService.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"} 