from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class Inversion(Base):
    __tablename__ = "inversiones"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String(10), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_compra = Column(Float, nullable=False)
    fecha_compra = Column(Date, nullable=False)
    sector = Column(String(30), nullable=False)
    observaciones = Column(String(200), nullable=True)