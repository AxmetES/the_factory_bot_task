import os

from environs import Env

env = Env()
env.read_env()


class Settings:
    SECRET_KEY = os.environ.get("SECRET_KEY")

    POSTGRES_USER = env.str('POSTGRES_USER', 'admin')
    POSTGRES_PASSWORD = env.str('POSTGRES_PASSWORD', 'admin')
    POSTGRES_DB = env.str('POSTGRES_DB', 'db')
    POSTGRES_HOST = env.str('POSTGRES_HOST', 'localhost')

    BOT_TOKEN = env('BOT_KEY', '6071706515:AAGop_V1FvT7YkIhaSRDPHeJJqQcAy8B6xk')


settings = Settings()
os.makedirs('logs', exist_ok=True)
