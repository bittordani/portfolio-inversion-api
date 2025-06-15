from pydantic import BaseModel
from datetime import date

class Inversion(BaseModel):
    id: int
    ticker: str
    cantidad: int
    precio_compra: float
    fecha_compra: date
    sector: str
    observaciones: str