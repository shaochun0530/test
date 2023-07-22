from test.web.api import dummy, echo, kafka, monitoring

from fastapi.routing import APIRouter

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
api_router.include_router(kafka.router, prefix="/kafka", tags=["kafka"])
