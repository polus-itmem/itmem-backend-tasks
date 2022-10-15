from enum import Enum
from sqlalchemy import Column, Integer, Enum as Enum_s, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Template(Base):
    __tablename__ = 'template'

    id = Column(Integer, primary_key = True)
    data = Column(Text, nullable = False)
