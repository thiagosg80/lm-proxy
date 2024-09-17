from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .get_env_config import get_env_config


def set_cors(app: FastAPI) -> None:
    config: dict = get_env_config()
    origins: list = config['CORS_ALLOWED_ORIGINS'].split(',')

    app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                       allow_headers=["*"])
