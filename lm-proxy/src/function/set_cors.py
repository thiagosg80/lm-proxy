from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values


def set_cors(app: FastAPI) -> None:
    config: dict = dotenv_values('../../.env')
    origins: list = config['CORS_ALLOWED_ORIGINS'].split(',')

    app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                       allow_headers=["*"])
