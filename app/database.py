# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Datos de conexión a tu base de datos MariaDB/MySQL
DB_USER = "fastapi_user"
DB_PASSWORD = "fastapi123"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "inversiones_db"

# URL de conexión
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear el motor y el SessionLocal
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos ORM
Base = declarative_base()
