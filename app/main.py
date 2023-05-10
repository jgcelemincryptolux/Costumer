
from fastapi import FastAPI
from routers import costumer



app = FastAPI()


app.include_router(costumer.router)


