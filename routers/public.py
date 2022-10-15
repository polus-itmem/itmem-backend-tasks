from fastapi import APIRouter, Request
import models

router = APIRouter()


@router.get('/test', response_model = models.Test)
async def add_cars(request: Request):
    session = request.scope['session']
