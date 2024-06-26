#!/usr/bin/python3
"""This module defines a class User"""
import models
from models.base_model import BaseModel
from sqlalchemy.orm import backref, relationship
from sqlalchemy import Column, String


class User(BaseModel,Base):
    """This class defines a user by various attributes"""
    if models.storage_type == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", cascade="all, delete-orphan",
                              backref="user")

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
