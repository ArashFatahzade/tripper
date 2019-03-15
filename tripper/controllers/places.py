from nanohttp import json
from restfulpy.controllers import ModelRestController, DBSession
from sqlalchemy_media import store_manager

from ..models import Place


class PlaceController(ModelRestController):
    __model__ = Place

    @store_manager(DBSession)
    @json
    @Place.expose
    def list(self):
        return DBSession.query(Place)
