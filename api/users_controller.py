import json
from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import FileResponse
from pydantic import BaseModel
import models.user as User
import jwt

UserRouter = APIRouter()

SECRET_KEY = "IsYouThere"
ALGORITHM = "HS256"

class LoginRequest(BaseModel):
    username: str
    password: str

class UserCreateRequest(BaseModel):
    username: str
    email: str
    password: str
    
# Route pour la page de création d'utilisateur
@UserRouter.get("/")
async def create_user_page():
    """Renvoie la page de création"""
    return FileResponse("static/html/create_user.html")

# Route pour créer un utilisateur
@UserRouter.post("/")
async def add_user(user_data: UserCreateRequest):
    """Ajoute un nouvel utilisateur"""
    try:
        new_user = User.add(user_data.username, user_data.email, user_data.password)
        return {"message": "Utilisateur ajouté avec succès", "user": new_user.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'ajout de l'utilisateur : {str(e)}")

# Route pour récupérer un utilisateur par son ID
@UserRouter.get("/get/{user_id}")
async def get_user(user_id: int):
    """Récupère un utilisateur par son identifiant"""
    user = User.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return {"user": user.to_dict()}

# Route pour la page de connexion
@UserRouter.get("/login")
async def login_page():
    """Renvoie la page de connexion"""
    return FileResponse("static/html/login.html")

# Route de connexion
@UserRouter.post("/login")
async def login_user(data: LoginRequest):
    print(data)
    """Authentifie un utilisateur et retourne un token"""
    user = User.get_by_username(data.username)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    if user.password != data.password:
        raise HTTPException(status_code=401, detail="Mot de passe incorrect")
    
    token = jwt.encode({"username": user.username}, SECRET_KEY, ALGORITHM)
    response = Response(content=json.dumps({"message": "Connexion réussie"}))
    response.set_cookie(key="login_token", value=token, httponly=True, samesite="Strict")
    return response

# Route protégée nécessitant un token
@UserRouter.get("/{user_id}/dashboard")
async def protected(request: Request):
    """Vérifie si l'utilisateur est authentifié via un cookie"""
    token = request.cookies.get("login_token")
    if not token:
        raise HTTPException(status_code=401, detail="Token manquant ou expiré")
    payload = jwt.decode(token, SECRET_KEY, ALGORITHM)

    return FileResponse("static/html/dashboard.html")
