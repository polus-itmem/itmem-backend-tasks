from typing import List

from fastapi import APIRouter, Request

import models
from services.web_query import WebQueryController

router = APIRouter()


@router.post('/create', response_model = models.Task)
async def create_task(request: Request, task_credit: models.TaskCredit):
    session: WebQueryController = request.scope['session']
    task = await session.add_task(
        date = task_credit.date,
        place = task_credit.place,
        user_id = task_credit.user_id,
    )
    return models.Task(
        id = task.task_id,
        user_id = task.user_id,
        date = task.date,
        place = task.place,
        allow = False
    )


@router.get('/all', response_model = List[models.Task])
async def get_tasks(request: Request):
    session: WebQueryController = request.scope['session']
    tasks = await session.get_tasks()
    return [models.Task(
        id = i.task_id,
        user_id = i.user_id,
        date = i.date,
        place = i.place,
        allow = True if i.allow else False
    ) for i in tasks]


@router.post('/user', response_model = List[models.Task])
async def get_user_tasks(request: Request, user_id: models.User):
    session: WebQueryController = request.scope['session']
    tasks = await session.get_user_task(user_id.id)
    return [models.Task(
        id = i.task_id,
        user_id = i.user_id,
        date = i.date,
        place = i.place,
        allow = True if i.allow else False
    ) for i in tasks]

