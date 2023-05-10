from typing import Union
from datetime import date
from pydantic import BaseModel


class Costumer(BaseModel):
    id: int
    name: str
    gender :str
    birthdate: date
    email:str
    address:str
    country:str
    departamento:str
    city: str

    class Config:
        orm_mode = True