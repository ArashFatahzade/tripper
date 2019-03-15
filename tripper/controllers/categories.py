from nanohttp import json
from restfulpy.controllers import ModelRestController, DBSession

from ..models import Category


class CategoryController(ModelRestController):
    __model__ = Category

    @json
    @Category.expose
    def list(self):
        return DBSession.query(Category)
