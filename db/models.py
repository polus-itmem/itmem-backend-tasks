from enum import Enum
from sqlalchemy import Column, Integer, Enum as Enum_s, Text, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class TaskStatus(Enum):
    finished = -1
    wait = 0
    process = 1


class Task(Base):
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key = True)
    user_id = Column(Integer, nullable = False)

    date = Column(Date, nullable = False)
    place = Column(Text, nullable = False)

    allow = relationship("DispatcherAllow", back_populates = "task", uselist = False, lazy='joined')
    car = relationship("TaskCar", back_populates = "task", uselist = False, lazy='joined')


class DispatcherAllow(Base):
    __tablename__ = 'allows'

    task_id = Column(ForeignKey('tasks.task_id'), primary_key = True)
    dispatcher_id = Column(Integer, nullable = False)
    status = Column(Enum_s(TaskStatus), default = TaskStatus.wait)

    task = relationship("Task", back_populates = "allow", uselist = False, lazy='joined')


class TaskCar(Base):
    __tablename__ = 'task_car_plan'

    task_id = Column(ForeignKey('tasks.task_id'), nullable = False)
    car_id = Column(Integer, primary_key = True)

    task = relationship("Task", back_populates = "car", uselist = False, lazy='joined')
