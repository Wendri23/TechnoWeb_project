from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware


from api.users import UserRouter


app = FastAPI()

# Autoriser les requêtes depuis le front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# crée une route qui charge un fichier html
@app.get("/")
def read_root():
  return RedirectResponse("/users/login", status_code=308)


# crée un router nommé UserRouter pour gérer les routes utilisateur
app.include_router(UserRouter, prefix="/users", tags=["users"])


# http://127.0.0.1:8000/docs