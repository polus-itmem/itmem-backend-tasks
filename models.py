from enum import Enum
from datetime import date
from typing import List, Optional
from strenum import StrEnum

from pydantic import BaseModel


class User(BaseModel):
    id: int


class TaskCredit(BaseModel):
    date: date
    place: str
    user_id: int


class Task(BaseModel):
    id: int

    date: date
    user_id: int
    place: str
    allow: bool
