from restfulpy.orm import DeclarativeBase, Field, relationship
from sqlalchemy import Integer, Unicode


class Category(DeclarativeBase):
    __tablename__ = 'category'

    id = Field(Integer, primary_key=True)

    name = Field(Unicode(30), unique=True)

    places = relationship('Place', back_populates='category')
