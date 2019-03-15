from restfulpy.orm import DeclarativeBase, Field, FilteringMixin, \
    PaginationMixin, OrderingMixin
from sqlalchemy import Integer, Unicode, JSON, FLOAT

from .images import PlaceImageList


class Place(FilteringMixin, OrderingMixin, PaginationMixin, DeclarativeBase):
    __tablename__ = 'place'

    id = Field(Integer, primary_key=True)
    name = Field(Unicode(30))
    description = Field(Unicode(2000), nullable=True)
    address = Field(Unicode(1000))
    latitude = Field(FLOAT)
    longitude = Field(FLOAT)
    images = Field(PlaceImageList.as_mutable(JSON), default=PlaceImageList())
