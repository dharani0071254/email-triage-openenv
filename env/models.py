from pydantic import BaseModel
from typing import List, Optional, Literal

class VisibleEmail(BaseModel):
    id: str
    subject: str
    content: str
    handled: bool

class Email(BaseModel):
    id: str
    subject: str
    content: str
    true_priority: Literal["high", "medium", "low"]
    handled: bool = False

class Observation(BaseModel):
    emails: List[VisibleEmail]
    time_remaining: int

class Action(BaseModel):
    action_type: Literal["classify", "respond", "ignore", "schedule"]
    email_id: str
    priority: Optional[Literal["high", "medium", "low"]] = None
    message: Optional[str] = None
    time: Optional[str] = None

class Reward(BaseModel):
    value: float