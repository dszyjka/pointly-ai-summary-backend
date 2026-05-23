from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database.models import SummaryRecord


async def run(user_id: str, searched_file: str, db: AsyncSession):
    results = await db.execute(
        select(SummaryRecord).where(
            SummaryRecord.user_id == user_id,
            SummaryRecord.filename.ilike(f'%{searched_file}%')
            )
        )
    records = results.scalars().all()
    return records