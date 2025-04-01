from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime

# Configuration de la base de données
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Définition des tables
class User(Base):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, nullable=False)
  email = Column(String, unique=True, nullable=False)
  password = Column(String, nullable=False)
  created_at = Column(DateTime, default=datetime.now())
  
  def to_dict(self):
    return {
        "id": self.id,
        "username": self.username,
        "email": self.email,
        "created_at": self.created_at
    }

# Création des tables
Base.metadata.create_all(engine)

# Exemple d'ajout d'un utilisateur
def add_user(name: str, email: str, password: str):
  session = SessionLocal()
  new_user = User(username=name, email=email, password=password)
  session.add(new_user)
  session.commit()
  session.refresh(new_user)
  session.close()
  return new_user

def get_user_by_id(user_id: int):
  session = SessionLocal()
  user = session.query(User).filter(User.id == user_id).first()
  session.close()
  return user

def get_user_by_username(username: str):
  session = SessionLocal()
  user = session.query(User).filter(User.username == username).first()
  session.close()
  return user