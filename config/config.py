import os


class Config:
    Base_url = os.getenv("Base_url")
    user_name = os.getenv("User_Name")
    password = os.getenv("Password")