from fastapi import APIRouter, HTTPException, Request, Response
import config.db as db
import json

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
@UserRouter.get("/get/{user_id}")
async def get_user(user_id: int):
    user = db.get_user_by_id(user_id)
    if not user:
      raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    return {
        "user": {
            "id": user[0],
            "username": user[1],
            "email": user[2],
            "password": user[3]
        }
    }
    
@UserRouter.post("/login")
async def login_user(username: str, password: str) -> Response:
    if not username or not password:
        raise HTTPException(
            status_code=400, 
            detail="Les champs 'username' et 'password' sont requis."
        )
    print(username)
    user = db.get_user_by_username(username)
    if not user:
      raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    if user[3] == password:
        token = "TOKEN"
        response = Response(content=json.dumps({"message": "Connexion reussie"}))
        response.set_cookie(key="login_token", value=token, httponly=True, samesite="Strict")
        return response
    
    raise HTTPException(status_code=401, detail="Mot de passe incorrect")

@UserRouter.get("/protected")
async def protected(request: Request) -> Response:
    token = request.cookies.get("login_token")
    if not token:
        raise HTTPException(status_code=401, detail="Token manquant ou expiré")

    if token != "TOKEN":
        raise HTTPException(status_code=401, detail="Token invalide")
    
    response = Response(content=json.dumps({"message": "Accès autorisé à la route protégée"}), media_type="application/json")
    return response