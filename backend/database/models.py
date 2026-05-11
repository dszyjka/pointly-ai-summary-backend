from sqlmodel import SQLModel, Field
from datetime import datetime


class SummaryRecord(SQLModel, table=True):
    id: int = Field(primary_key=True)
    user_id: str
    filename: str
    response_type: str
    summary: str
    created_at: datetime = Field(default_factory=datetime.now)