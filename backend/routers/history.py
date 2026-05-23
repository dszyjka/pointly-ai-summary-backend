from fastapi import APIRouter, Depends
from backend.database.database import get_db
from backend.services import history
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from backend.database.models import SummaryRecord

router = APIRouter()

@router.get('/history/{user_id}', response_model=List[SummaryRecord])
async def get_history(user_id: str, db: AsyncSession = Depends(get_db)):
    return await history.run(user_id, db)