import time

from sqlalchemy import select


class WebQueryController:
    def __init__(self, session):
        self._session = session

