from fastapi import APIRouter, HTTPException, Request, Depends
import jwt
from datetime import datetime, timedelta
import config.db as db

UserRouter = APIRouter()

# route pour creer un user
@UserRouter.post("/")
async def add_user(request: Request, username: str, email: str, password: str):
    # pour le moment les info users sont en params de la fonction mais a terme ils seront rensegner dans un formulaire et envoyer auformat json 
    """Récupérer les données JSON envoyées dans le corps de la requête
    data = await request.json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")"""

    if not username or not email or not password:
        raise HTTPException(
            status_code=400, 
            detail="Les champs 'username', 'email' et 'password' sont requis."
        )
    
    try:
        db.add_user(username, email, password)
        return {"message": "Utilisateur ajouté avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'ajout de l'utilisateur : {e}")

# route pour get un user
@UserRouter.get("/{user_id}")
async def get_user(user_id: int):
    user = db.get_user(user_id)
    if not user:
      raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    return {
        "user": {
            "id": user[0],
            "username": user[1],
            "email": user[2]
        }
    }

# route de connexion utilisateur
@UserRouter.post("/login")
async def login_user(username: str, password: str, role: str):
    