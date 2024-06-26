#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import Base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_type == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(string(60), ForeignKey('user.id'), nullable=False)
        name = Column(string(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade="all, delete-orphan",
                               backref="place")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def reviews(self):
        """getter attribute reviews that returns the list of Review"""
        reviews_list = []
        for review in storage.all("Review").values():
            if review.place_id == self.id:
                reviews_list.append(review)
        return reviews_list
