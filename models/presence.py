from sqlalchemy.orm import Session
from models.db import SessionLocal, engine, Presence
from datetime import datetime

Presence.metadata.create_all(engine)

def create_presence(user_id: int, event_id: int, status: str):
    session: Session = SessionLocal()
    db_presence = Presence(user_id=user_id, event_id=event_id, status=status, timestamp=datetime.now())
    session.add(db_presence)
    session.commit()
    session.refresh(db_presence)
    return db_presence