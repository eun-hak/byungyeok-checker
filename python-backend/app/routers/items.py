from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.services.item_service import ItemService

router = APIRouter()

@router.get("/", response_model=List[Item])
async def get_items():
    """모든 아이템 목록 조회"""
    return ItemService.get_all_items()

@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """특정 아이템 조회"""
    item = ItemService.get_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=Item)
async def create_item(item: ItemCreate):
    """새 아이템 생성"""
    return ItemService.create_item(item)

@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemUpdate):
    """아이템 정보 업데이트"""
    updated_item = ItemService.update_item(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/{item_id}")
async def delete_item(item_id: int):
    """아이템 삭제"""
    success = ItemService.delete_item(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"} 