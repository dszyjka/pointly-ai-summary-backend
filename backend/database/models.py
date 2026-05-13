from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class SummaryRecord(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: str = Field(index=True)
    filename: str
    summary: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))