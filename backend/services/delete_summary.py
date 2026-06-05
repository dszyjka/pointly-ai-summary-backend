from backend.database.models import SummaryRecord
from sqlmodel import delete
from sqlalchemy.ext.asyncio import AsyncSession


async def run(db: AsyncSession, summary_id: int):
    await db.execute(delete(SummaryRecord).where(SummaryRecord.id == summary_id))
    await db.commit()