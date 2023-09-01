import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.crawling.crawling import lyrics_crawling

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, "../.env"))
origins_host = os.environ["ORIGINS_HOST"]

origins = [origins_host]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lyrics_crawling)

# search_songs()
# organization_result()
# drop_duplicate_result()
