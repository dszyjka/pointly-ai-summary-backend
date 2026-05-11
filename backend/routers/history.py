from fastapi import APIRouter, Depends
from sqlmodel import Session
from database.database import get_db
from services import history
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()

@router.get('/history/{user_id}')
async def get_history(user_id: str, db: AsyncSession = Depends(get_db)):
    return await history.get_history(user_id, db)