from fastapi import File, UploadFile, Form, Depends
from fastapi.responses import StreamingResponse
from fastapi import APIRouter
from typing import Annotated
from database.database import get_db
from constants.labels import ResponseType
from services import summarize
from sqlalchemy.ext.asyncio import AsyncSession
from google import genai
from config import Settings


router = APIRouter()
settings = Settings()


@router.post('/summarize') # multipart/form-data
async def post_summarize(
                file: Annotated[UploadFile, File()],
                response_type: Annotated[ResponseType, Form()],
                user_rules: Annotated[list[str], Form()],
                user_id: Annotated[str, Form()],
                db: AsyncSession = Depends(get_db),
                    ):

    return StreamingResponse(await summarize.run(file, user_id, response_type, user_rules, db), media_type='text/plain')