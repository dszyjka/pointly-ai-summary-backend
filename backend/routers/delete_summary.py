from fastapi import APIRouter, Depends
from backend.database.database import get_db
from backend.services import delete_summary
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()

@router.delete('/delete_summary')
async def del_summary(summary_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_summary.run(db, summary_id)