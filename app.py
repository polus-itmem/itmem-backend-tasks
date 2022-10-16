import asyncio
import time

import uvicorn
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from config import config
from db import create_connect
from middlewares import session
from routers import router

app = FastAPI(title = 'Tasks', version = '1.1.0')


@app.get("/", description = "Server time", response_model = int)
async def time_check():
    return time.time()

engine = create_connect.create_connection(config.db.get_secret_value())
app.add_middleware(BaseHTTPMiddleware,
                   dispatch = session.SessionMiddleware(
                       engine = engine
                   ))
asyncio.run(create_connect.create_all(engine))
app.include_router(router)

uvicorn.run(app, host = config.host, port = config.port)
