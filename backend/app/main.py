from fastapi import FastAPI
from app.api.v1.endpoints import auth, alerts, devices
from app.db.session import Base, engine

# Crear las tablas de la base de datos automáticamente (solo para desarrollo)
Base.metadata.create_all(bind=engine)

# Inicializar la aplicación FastAPI
app = FastAPI(
    title="SafeNest API",
    description="API para gestionar usuarios, dispositivos y alertas de SafeNest",
    version="1.0.0"
)

# Incluir los routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(alerts.router, prefix="/api/v1/alerts", tags=["Alerts"])
app.include_router(devices.router, prefix="/api/v1/devices", tags=["Devices"])

# Ruta de prueba
@app.get("/")
def root():
    return {"message": "Bienvenido a la API de SafeNest"}
