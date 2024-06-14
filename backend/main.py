from fastapi import FastAPI
from starlette import status
from starlette.middleware.cors import CORSMiddleware

from web.api.routes import router as api_router

HTTP_422 = status.HTTP_422_UNPROCESSABLE_ENTITY

app = FastAPI(title="OverseasOps Lab API", debug=True)

app.add_middleware(CORSMiddleware, allow_origins=['*'])

app.include_router(api_router, prefix="/api")


@app.on_event("startup")
async def startup():
    pass


@app.get("/", include_in_schema=False)
async def health():
    return {"message": "Welcome to OverseasOps Lab"}
