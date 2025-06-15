from app.modelos import Inversion
from datetime import date

inversiones = [
    Inversion(
        id=1,
        ticker="AAPL",
        cantidad=10,
        precio_compra=150.0,
        fecha_compra="2024-01-15",
        sector="tecnología",
        observaciones="Compra a largo plazo"
    ),
    Inversion(
        id=2,
        ticker="MSFT",
        cantidad=5,
        precio_compra=310.0,
        fecha_compra="2024-03-02",
        sector="tecnología",
        observaciones="Buena previsión de resultados"
    )
]