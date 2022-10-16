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
        cars_ids = task_credit.cars_ids
    )
    return models.Task(
        id = task.task_id,
        user_id = task.user_id,
        date = task.date,
        place = task.place,
        moderate = None if not task.allow else models.TaskModerate(dispatcher_id = task.allow.dispatcher_id,
                                                                   status = task.allow.status),
        car_id = task.car.car_id
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
        moderate = None if not i.allow else models.TaskModerate(dispatcher_id = i.allow.dispatcher_id,
                                                                status = i.allow.status),
        car_id = i.car.car_id
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
        moderate = None if not i.allow else models.TaskModerate(dispatcher_id = i.allow.dispatcher_id,
                                                                status = i.allow.status),
        car_id = i.car.car_id
    ) for i in tasks]


@router.post('/car', response_model = List[models.Task])
async def cars_tasks(request: Request, car_ids: List[models.ModelId]):
    session: WebQueryController = request.scope['session']
    tasks = await session.get_cars_task([i.id for i in car_ids])
    return [models.Task(
        id = i[0].task_id,
        user_id = i[0].user_id,
        date = i[0].date,
        place = i[0].place,
        moderate = None if not i[0].allow else models.TaskModerate(dispatcher_id = i[0].allow.dispatcher_id,
                                                                   status = i[0].allow.status),
        car_id = i[1].car_id
    ) for i in tasks]


@router.post('/change', response_model = models.Task)
async def create_task(request: Request, allow_credit: models.DispatcherAllowCredits):
    session: WebQueryController = request.scope['session']
    task = await session.accept_task(
        task_id = allow_credit.task_id,
        dispatcher_id = allow_credit.dispatcher_id,
        status = allow_credit.status
    )
    return models.Task(
        id = task.task_id,
        user_id = task.user_id,
        date = task.date,
        place = task.place,
        moderate = None if not task.allow else models.TaskModerate(dispatcher_id = task.allow.dispatcher_id,
                                                                   status = task.allow.status),
        car_id = task.car.car_id
    )
