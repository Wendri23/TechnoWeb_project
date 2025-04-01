from fastapi import FastAPI
from fastapi.responses import FileResponse

from api.users import UserRouter


app = FastAPI()

# crée une route qui charge un fichier html
@app.get("/")
def read_root():
  return FileResponse("static/html/login.html")


# crée un router nommé UserRouter pour gérer les routes utilisateur
app.include_router(UserRouter, prefix="/users", tags=["users"])


# http://127.0.0.1:8000/docs