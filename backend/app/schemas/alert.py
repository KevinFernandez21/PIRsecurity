from pydantic import BaseModel

class AlertBase(BaseModel):
    id_evento: int
    mensaje: str
    nivel_alerta: str

class AlertOut(AlertBase):
    id: int

    class Config:
        orm_mode = True
