from sqlalchemy.orm import Session
from models.db import SessionLocal, engine, User

User.metadata.create_all(engine)

# Fonctions pour gérer les utilisateurs
def add(name: str, email: str, password: str):
    session: Session = SessionLocal()
    new_user = User(username=name, email=email, password=password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    session.close()
    return new_user

def get_by_id(user_id: int):
    session: Session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    return user

def get_by_username(username: str):
    session: Session = SessionLocal()
    user = session.query(User).filter(User.username == username).first()
    session.close()
    return user
