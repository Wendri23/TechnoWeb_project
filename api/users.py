from fastapi import APIRouter, HTTPException, Request
from config.db import add_user, get_user

UserRouter = APIRouter()

@UserRouter.post("/")
async def add_users(request: Request, username: str, email: str, password: str):
    # Récupérer les données JSON envoyées dans le corps de la requête
    # data = await request.json()
    # username = data.get("username")
    # email = data.get("email")
    # password = data.get("password")

    # Validation manuelle des champs requis
    if not username or not email or not password:
        raise HTTPException(
            status_code=400, 
            detail="Les champs 'username', 'email' et 'password' sont requis."
        )
    
    try:
        add_user(username, email, password)
        return {"message": "Utilisateur ajouté avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'ajout de l'utilisateur : {e}")

@UserRouter.get("/{user_id}")
async def get_users(user_id: int):
    user = get_user(user_id)
    if not user:
      raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    return {
        "user": {
            "id": user[0],
            "username": user[1],
            "email": user[2]
        }
    }
