from fastapi import FastAPI
from function.get_chain import get_chain
from function.set_routes import set_routes
from function.set_cors import set_cors
from function.get_env_config import get_env_config
from langchain_core.runnables.base import Runnable

chain: Runnable = get_chain()
app: FastAPI = FastAPI()
set_cors(app)
set_routes(app, chain)

if __name__ == '__main__':
    import uvicorn

    server_port: int = int(get_env_config()['SERVER_PORT'])
    uvicorn.run(app, host='0.0.0.0', port=server_port)
