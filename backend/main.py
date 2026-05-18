from fastapi import FastAPI
from config import settings
from .database.database import init_db
from .routers import summarize, history
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(summarize.router, prefix='/api', tags=['summarization'])
app.include_router(history.router, prefix='/api', tags=['history'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)