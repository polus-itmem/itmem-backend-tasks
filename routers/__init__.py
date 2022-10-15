from fastapi import APIRouter

from . import public


router = APIRouter(prefix = '/template')

router.include_router(public.router, prefix="/public")
