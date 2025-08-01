import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_USER     = os.getenv("DB_USER",     "fastapi_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "fastapi_pass")
DB_HOST     = os.getenv("DB_HOST",     "db")          #  <- NOMBRE DEL SERVICIO
DB_PORT     = os.getenv("DB_PORT",     "3306")
DB_NAME     = os.getenv("DB_NAME",     "inversiones_db")

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine        = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal  = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base          = declarative_base()
