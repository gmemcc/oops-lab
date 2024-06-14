import logging

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from backend.models.base import Base
from backend.db import async_engine
from backend.web.api.routes import router as api_router
from fastapi_pagination import add_pagination

HTTP_422 = status.HTTP_422_UNPROCESSABLE_ENTITY

app = FastAPI(title="OverseasOps API", debug=True, responses={
    HTTP_422: {"description": "Validation Error", "content": {"application/json": {"example": {
        "success": False,
        "code": 42200,
        "msgid": "validation.error",
        "showType": 2,
        "data": [{
            "loc": [
                "string",
                0
            ],
            "msg": "string",
            "type": "string"
        }]
    }}}},
})

app.add_middleware(CORSMiddleware, allow_origins=['*'])

app.include_router(api_router, prefix="/api")

add_pagination(app)

logger = logging.getLogger(__name__)


@app.on_event("startup")
async def startup():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/", include_in_schema=False)
async def health():
    return {"message": "Welcome to OverseasOps Lab"}
