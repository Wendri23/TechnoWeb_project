from sqlalchemy.orm import Session
from models.db import SessionLocal, engine, Presence, User
from datetime import datetime

Presence.metadata.create_all(engine)

def create_presence(user_id: int, event_id: int, status: str):
    session: Session = SessionLocal()
    db_presence = Presence(user_id=user_id, event_id=event_id, status=status, timestamp=datetime.now())
    session.add(db_presence)
    session.commit()
    session.refresh(db_presence)
    return db_presence

def get_users_present_for_event(event_id: int):
    session: Session = SessionLocal()
    presences = (
        session.query(User)
        .join(Presence)
        .filter(Presence.event_id == event_id, Presence.status == "présent")
        .all()
    )
    session.close()
    return [user.to_dict() for user in presences]