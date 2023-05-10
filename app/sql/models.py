from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Float, Date
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Costumer(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True, autoincrement= True)
    name = Column(String(255), unique=True,)
    gender = Column(String(255), unique=True,)
    birthdate = Column(Date, nullable=False)
    email = Column(String(255), unique=True,)
    address = Column(String(255), unique=True,)
    country = Column(String(255), unique=True,)
    departamento = Column(String(255), unique=True,)
    city = Column(String(255), unique=True,)

