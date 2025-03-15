from fastapi import FastAPI
from fastapi.responses import FileResponse

from config.db import init_db
from api.users import UserRouter


app = FastAPI()

# appel a la fonction pour initialiser la base de données
init_db()

# crée une route qui charge un fichier html
@app.get("/")
def read_root():
  return FileResponse("static/index.html")

# crée un router nommé UserRouter pour gérer les routes utilisateur
app.include_router(UserRouter, prefix="/users", tags=["users"])


# http://127.0.0.1:8000/docs