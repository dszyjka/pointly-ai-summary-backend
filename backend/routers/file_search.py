from fastapi import APIRouter, Depends
from backend.services import file_search
from backend.database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from backend.database.models import SummaryRecord
from backend.routers.summarize import get_user_from_header


router = APIRouter()

@router.get('/search', response_model=List[SummaryRecord])
async def search_files(searched_file: str,
                       user_id: str = Depends(get_user_from_header),
                       db: AsyncSession = Depends(get_db)):
    return await file_search.run(user_id, searched_file, db)