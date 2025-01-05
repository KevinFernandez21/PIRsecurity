from fastapi import APIRouter
from app.api.v1.endpoints import auth, alerts, devices

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])
api_router.include_router(devices.router, prefix="/devices", tags=["Devices"])
