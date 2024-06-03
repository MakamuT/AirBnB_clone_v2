#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
if models.storage_type == "db":
    __tablename__ = 'states'
    name = Column(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete-orphan", backref="state")
    else:
	name = ""

	def __init__(self, *args, **kwargs):
            """initialize state"""
            super().__init__(*args, **kwargs)

        if models.storage_t != "db":
           @property
           def cities(self):
               """getter attribute cities that returns the list of City"""
               from models import storage
               cities_list = []
               all_cities = models.storage.all(City)
               for city in storage.all(City).values():
                   if city.state_id == self.id:
                      cities_list.append(city)
               return cities_list
