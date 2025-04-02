from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Enum
from datetime import datetime
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Configuration de la base de données
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Définition de la table User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    events = relationship("Event", back_populates="creator", cascade="all, delete")
    presences = relationship("Presence", back_populates="user", cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat()
        }

# Définition de la table Event
class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    locality = Column(String, nullable=False)
    creator_id = Column(Integer, ForeignKey("users.id"), index=True)
    created_at = Column(DateTime, default=datetime.now)

    creator = relationship("User", back_populates="events")
    presences = relationship("Presence", back_populates="event", cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date": self.date.isoformat(),
            "locality": self.locality,
            "created_at": self.created_at.isoformat(),
            "creator_id": self.creator_id
        }

# Définition de la table Presence
class Presence(Base):
    __tablename__ = "presences"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    event_id = Column(Integer, ForeignKey("events.id"), index=True)
    status = Column(Enum("présent", "absent", "indécis", name="status_enum"), nullable=False)
    timestamp = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates="presences")
    event = relationship("Event", back_populates="presences")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "event_id": self.event_id,
            "status": self.status,
            "timestamp": self.timestamp.isoformat()
        }

# Création des tables
Base.metadata.create_all(engine)
