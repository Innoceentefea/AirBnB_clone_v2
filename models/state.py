#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship(
            'City',
            cascade='all, delete-orphan',
            backref='state'
        )
    else:
        @property
        def cities(self):
            """Getter attribute to retrieve a list of City instances"""
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
