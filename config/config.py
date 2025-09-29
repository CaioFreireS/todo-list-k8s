import os
from dotenv import load_dotenv
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.resolve()
ENV_PATH = BASE_DIR / 'db.env'

load_dotenv(ENV_PATH) 

class Config:
    DB_HOST = os.environ.get('DB_HOST') 
    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')
    
    FLASK_ENV = os.environ.get('FLASK_ENV')