#!/usr/bin/python3

"""

This module defines a State class

"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    A State class
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128))

    def __repr__(self):
        return f'{self.id}: {self.name}'
