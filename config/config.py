import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    Base_url = os.getenv("BASE_URL")
    user_name = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")