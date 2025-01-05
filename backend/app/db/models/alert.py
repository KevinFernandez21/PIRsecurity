from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.db.session import Base

class Alert(Base):
    __tablename__ = "alertas"

    id = Column(Integer, primary_key=True, index=True)
    id_evento = Column(Integer, ForeignKey("eventos.id"), nullable=False)
    mensaje = Column(String(255), nullable=False)
    nivel_alerta = Column(Enum("bajo", "medio", "alto"), nullable=False)
    fecha_alerta = Column(DateTime, default=func.now())
