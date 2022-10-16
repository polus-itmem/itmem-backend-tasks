from datetime import date as Date

from sqlalchemy import select

import models
from db.models import Task, TaskCar, DispatcherAllow


class WebQueryController:
    def __init__(self, session):
        self._session = session

    async def add_task(self, date: Date, place: str, user_id: int, cars_ids: [int]) -> Task:
        tasks = (await self._session.execute(select(Task).where(Task.date == date))).all()
        disallow_car_ids = [i[0].car.car_id for i in tasks]
        for i in cars_ids:
            if i not in disallow_car_ids:
                task = Task(date = date, place = place, user_id = user_id)
                self._session.add(task)
                await self._session.flush()
                task_car = TaskCar(task_id = task.task_id, car_id = i)
                self._session.add(task_car)
                await self._session.flush()
                task.car = task_car
                task.allow = None
                return task

    async def get_tasks(self):
        tasks: [Task] = (await self._session.execute(select(Task))).all()
        return [i[0] for i in tasks]

    async def get_user_task(self, user_id: int):
        tasks: [Task] = (await self._session.execute(select(Task).where(Task.user_id == user_id))).all()
        return [i[0] for i in tasks]

    async def get_cars_task(self, cars_id: [int]):
        tasks: [TaskCar] = (await self._session.execute(select(TaskCar).where(TaskCar.car_id.in_(cars_id)))).all()
        return [[i[0].task, i[0]] for i in tasks]

    async def accept_task(self, task_id: int, dispatcher_id: int, status: models.TaskStatus):
        task = await self._session.get(Task, task_id)
        if not task.allow:
            allow = DispatcherAllow(dispatcher_id = dispatcher_id, task_id = task.task_id)
            self._session.add(allow)
            await self._session.flush()
            task.allow = allow
        task.allow.status = status
        await self._session.flush()
        return task

