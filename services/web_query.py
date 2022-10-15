from datetime import date as Date

from sqlalchemy import select

from db.models import Task


class WebQueryController:
    def __init__(self, session):
        self._session = session

    async def add_task(self, date: Date, place: str, user_id: int) -> Task:
        task = Task(date = date, place = place, user_id = user_id)
        self._session.add(task)
        await self._session.flush()
        return task

    async def get_tasks(self):
        tasks: [Task] = (await self._session.execute(select(Task))).all()
        return [i[0] for i in tasks]

    async def get_user_task(self, user_id: int):
        tasks: [Task] = (await self._session.execute(select(Task).where(Task.user_id == user_id))).all()
        return [i[0] for i in tasks]
