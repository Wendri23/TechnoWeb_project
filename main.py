from fastapi import FastAPI

from config.db import init_db
from api.users import UserRouter


app = FastAPI()

init_db()

@app.get("/")
def read_root():
  return {"Hello": "World"}

app.include_router(UserRouter, prefix="/users", tags=["users"])
