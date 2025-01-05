from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.sensor import SensorBase, SensorOut
from app.db.models.sensor import Sensor

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SensorOut)
def create_device(sensor: SensorBase, db: Session = Depends(get_db)):
    db_sensor = Sensor(**sensor.dict())
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

@router.get("/{sensor_id}", response_model=SensorOut)
def get_device(sensor_id: int, db: Session = Depends(get_db)):
    db_sensor = db.query(Sensor).filter(Sensor.id == sensor_id).first()
    if not db_sensor:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return db_sensor
