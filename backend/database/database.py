from sqlmodel import SQLModel
from config import Settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker


settings = Settings()
engine = create_async_engine(settings.database_url, echo=True)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
 
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_db():
    async with async_session() as session:
        yield session

async def save_to_db(db, record):
    db.add(record)
    await db.commit()