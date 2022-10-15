from fastapi import APIRouter

from . import public


router = APIRouter(prefix = '/tasks')

router.include_router(public.router)
