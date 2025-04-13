from sqlalchemy.orm import Session
from models.db import SessionLocal, engine, Event
from datetime import datetime

Event.metadata.create_all(engine)

def add_event(event: Event):
    session: Session = SessionLocal()
    event = Event(
        title=event.title,
        description=event.description,
        date=event.date,
        locality=event.locality,
        created_at= datetime.now(),
        creator_id=event.creator_id
    )
    session.add(event)
    session.commit()
    session.refresh(event)
    session.close()

    return event

def get_by_id(event_id: int):
    session: Session = SessionLocal()
    event = session.query(Event).filter(Event.id == event_id).first()
    session.close()
    return event