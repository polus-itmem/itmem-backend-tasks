from enum import Enum
from typing import List, Optional
from strenum import StrEnum

from pydantic import BaseModel


class Test(BaseModel):
    data: str
