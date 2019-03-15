from nanohttp import json, int_or_notfound
from restfulpy.controllers import ModelRestController, DBSession
from sqlalchemy_media import store_manager

from ..models import Place


class PlaceController(ModelRestController):
    __model__ = Place

    @store_manager(DBSession)
    @json
    @Place.expose
    def get(self, id):
        id = int_or_notfound(id)
        return DBSession.query(Place).get(id)

    @store_manager(DBSession)
    @json
    @Place.expose
    def list(self):
        return DBSession.query(Place)
