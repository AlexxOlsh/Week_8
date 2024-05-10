from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class User(BaseModel):
    id: int
    username: str
    wallet: float
    birthdate: date


class UserUpdate(BaseModel):
    username: Optional[str] = None
    wallet: Optional[float] = None
    birthdate: Optional[date] = None
