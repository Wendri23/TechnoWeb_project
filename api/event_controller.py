from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import models.event as EventService
import models.presence as Presence
from datetime import datetime

EventRouter = APIRouter()

class EventCreateRequest(BaseModel):
    title: str
    description: str
    date: datetime
    locality: str
    creator_id: int

@EventRouter.get("/{event_id}")
async def get_event(event_id: int):
    """Récupérer un événement par son ID"""
    try:
        event = EventService.get_by_id(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Événement non trouvé")
        return event
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@EventRouter.post("/")
async def create_event(event_data: EventCreateRequest):
    """Créer un nouvel événement"""
    try:
        new_event = EventService.add_event(event_data)
        presence = Presence.create_presence(event_data.creator_id, new_event.id, "présent")
        return new_event
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))