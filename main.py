from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from api.users_controller import UserRouter
from api.event_controller import EventRouter

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates") #inverser les 2


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

# crée un router nommé EventRouter pour gérer les routes utilisateur
app.include_router(EventRouter, prefix="/events", tags=["events"])

# http://127.0.0.1:8000/docs