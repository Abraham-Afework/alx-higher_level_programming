#!/usr/bin/python3
"""
 python file that contains the class definition of a State \
         and an instance Base = declarative_base()

"""
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """
    Represents State

    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __int__(self, id, name):
        self.id = id
        self.name = name
