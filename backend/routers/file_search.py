from fastapi import APIRouter, Depends
from backend.services import file_search
from backend.database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from backend.database.models import SummaryRecord


router = APIRouter()

@router.get('/search-files/{user_id}/{searched_file}', response_model=List[SummaryRecord])
async def search_files(user_id: str, searched_file: str, db: AsyncSession = Depends(get_db)):
    return await file_search.run(user_id, searched_file, db)