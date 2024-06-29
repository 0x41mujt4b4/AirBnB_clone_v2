#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table amenities.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = ''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
    def __str__(self):
        """Return the string representation of this Amenity like this '[{name}] ({id}) {dictionary}'."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

