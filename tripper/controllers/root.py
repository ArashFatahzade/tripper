from nanohttp import Controller, json
from restfulpy.controllers import RootController

import tripper
from .places import PlaceController
from .categories import CategoryController


class APIv1Controller(Controller):

    categories = CategoryController()
    places = PlaceController()

    @json
    def version(self):
        return dict(version=tripper.__version__)


class Root(RootController):
    apiv1 = APIv1Controller()
