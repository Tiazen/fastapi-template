from fastapi import FastAPI

from app.database import Base, engine
from app.routers import stories, tasks

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)
# Import the dialog router

app.include_router(stories.router)
app.include_router(tasks.router)