from fastapi import File, UploadFile, Form, Depends, Header, HTTPException
from fastapi.responses import StreamingResponse
from fastapi import APIRouter
from typing import Annotated
from database.database import get_db
from constants.labels import ResponseType
from services import summarize
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()

async def get_user_from_header(x_user_id: str = Header(None)):
    if x_user_id is None:
        raise HTTPException(400, detail='Missing X-USER-ID header')
    return x_user_id

@router.post('/summarize') # multipart/form-data
async def post_summarize(
                file: Annotated[UploadFile, File()],
                response_type: Annotated[ResponseType, Form()],
                user_rules: Annotated[list[str], Form()],
                user_id: str = Depends(get_user_from_header),
                db: AsyncSession = Depends(get_db),
                    ):

    return StreamingResponse(summarize.run(file, user_id, response_type, user_rules, db), media_type='text/plain')