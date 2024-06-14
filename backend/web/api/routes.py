from fastapi import APIRouter

from .reports.routes import router as reporter_router

router = APIRouter()

router.include_router(reporter_router)
