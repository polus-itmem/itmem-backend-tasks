from datetime import date
from typing import List, Optional

from pydantic import BaseModel
from db.models import TaskStatus


class ModelId(BaseModel):
    id: int


class TaskModerate(BaseModel):
    dispatcher_id: int
    status: TaskStatus


class User(BaseModel):
    id: int


class TaskCredit(BaseModel):
    date: date
    place: str
    user_id: int
    cars_ids: List[int]


class Task(BaseModel):
    id: int

    date: date
    user_id: int
    place: str
    moderate: Optional[TaskModerate]
    car_id: Optional[int]


class DispatcherAllowCredits(BaseModel):
    dispatcher_id: int
    task_id: int
    status: TaskStatus
