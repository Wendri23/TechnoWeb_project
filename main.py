from fastapi import FastAPI
from fastapi.responses import FileResponse

from config.db import init_db
from api.users import UserRouter


app = FastAPI()

init_db()

@app.get("/")
def read_root():
  return FileResponse("static/index.html")

app.include_router(UserRouter, prefix="/users", tags=["users"])
