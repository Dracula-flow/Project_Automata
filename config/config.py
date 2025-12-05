import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config\.env")

class Config:

    BASE_URL = os.getenv('BASE_URL')
    USERNAME = os.getenv('APP_USERNAME')
    PASSKEY = os.getenv('PASSKEY')