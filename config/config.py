import os
from dotenv import load_dotenv
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent.resolve()
ENV_PATH = BASE_DIR / 'config' / 'db.env' 
load_dotenv(ENV_PATH) 

class Config:
    DB_HOST = os.environ.get('DB_HOST', 'postgres-service')
    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')
    
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )