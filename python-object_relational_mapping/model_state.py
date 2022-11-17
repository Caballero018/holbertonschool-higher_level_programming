#!/usr/bin/python3
"""
Module that have a class definition of a State and an instance.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    "Class definition of a State and an instance Base = declarative_base()"
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
