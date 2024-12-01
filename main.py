import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from handlers import router

from  db.requests import add_child, all_children, child_by_id, add_raven_test, add_emotion_test, remove_child_by_id

from models import Child, RavenTest, EmotionTest

from psychological_keys import raven_test_key, emotions_test_key

app = FastAPI()

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)