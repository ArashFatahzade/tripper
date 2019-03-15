from restfulpy.orm import DeclarativeBase, Field, FilteringMixin, \
    PaginationMixin, OrderingMixin, relationship
from sqlalchemy import Integer, Unicode, JSON, FLOAT, ForeignKey

from .images import PlaceImageList


class Place(FilteringMixin, OrderingMixin, PaginationMixin, DeclarativeBase):
    __tablename__ = 'place'

    id = Field(Integer, primary_key=True)

    category_id = Field(Integer, ForeignKey('category.id'), protected=True)

    name = Field(Unicode(30))
    description = Field(Unicode(2000), nullable=True)
    address = Field(Unicode(1000))
    latitude = Field(FLOAT)
    longitude = Field(FLOAT)
    images = Field(PlaceImageList.as_mutable(JSON), default=PlaceImageList())

    category = relationship(
        'Category',
        protected=False,
        foreign_keys=category_id,
        back_populates='places'
    )
