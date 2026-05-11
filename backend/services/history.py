from database.database import get_db
from database.models import SummaryRecord
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends


async def get_history(user_id: str, db: AsyncSession):
    records = await db.exec(select(SummaryRecord).where(SummaryRecord.user_id == user_id)).all()
    return records