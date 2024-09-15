from fastapi import FastAPI
from function.get_chain import get_chain
from function.set_routes import set_routes
from langchain_core.runnables.base import Runnable
from fastapi.middleware.cors import CORSMiddleware

chain: Runnable = get_chain()
app: FastAPI = FastAPI()
origins: list = ['http://localhost:4455']

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])

set_routes(app, chain)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)
