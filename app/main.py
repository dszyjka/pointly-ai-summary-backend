from fastapi import FastAPI, File, UploadFile, Form
from google import genai
from files_reading import extract_text
from typing import Annotated
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    gemini_api_key: str
    
    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI()

@app.post('/summarize') # multipart/form-data
async def summarize(
                file: Annotated[UploadFile, File()],
                response_type: Annotated[str, Form()],
                user_rules: Annotated[list[str], Form()]):

    client = genai.Client(api_key=settings.gemini_api_key)
    model = 'gemini-2.5-flash'

    text = await extract_text(file)

    response_rules = ''

    for rule in user_rules:
        response_rules += f'{rule}\n'

    response = await client.aio.models.generate_content(
        model=model,
        contents=
            f'''summarize the text below:\n\n{text}
            Response type: {response_type},
            Response rules:\n{response_rules}'''
    )

    return {'summary' : response.text}