from nanohttp import Controller, json
from restfulpy.controllers import RootController

import tripper


class APIv1Controller(Controller):

    @json
    def version(self):
        return dict(version=tripper.__version__)


class Root(RootController):
    apiv1 = APIv1Controller()
