import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config\.env")

class Config:

    BASE_URL = os.getenv('BASE_URL')
    
    USERNAME_VALID = os.getenv('APP_USERNAME_VALID')
    USERNAME_LOCKED_OUT = os.getenv('APP_USERNAME_LOCKED_OUT')
    USERNAME_PROBLEM = os.getenv('APP_USERNAME_PROBLEM')
    USERNAME_GLITCH = os.getenv('APP_USERNAME_GLITCH')
    USERNAME_ERROR = os.getenv('APP_USERNAME_ERROR')
    USERNAME_VISUAL = os.getenv('APP_USERNAME_VISUAL')
    
    PASSKEY = os.getenv('PASSKEY')