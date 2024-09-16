from fastapi import FastAPI
from function.get_chain import get_chain
from function.set_routes import set_routes
from function.set_cors import set_cors
from langchain_core.runnables.base import Runnable

chain: Runnable = get_chain()
app: FastAPI = FastAPI()
set_cors(app)
set_routes(app, chain)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)
