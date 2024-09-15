from fastapi import FastAPI
from .get_message import get_message


def set_routes(app: FastAPI, chain) -> None:
    @app.get('/messages')
    def get_messages_api(client_input: str) -> dict:
        return get_message(client_input, chain)
