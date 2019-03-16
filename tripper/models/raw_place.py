from restfulpy.orm import DeclarativeBase, Field
from sqlalchemy import Integer
from sqlalchemy.dialects.postgresql import JSONB


class RawPlace(DeclarativeBase):
    __tablename__ = 'raw_place'

    id = Field(Integer, primary_key=True)

    data = Field(JSONB)

