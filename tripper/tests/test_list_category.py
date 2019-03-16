
from bddrest import response, status

from tripper.models import Category

from .helpers import LocalApplicationTestCase


class TestCategory(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()

        categories = [
            Category(
                name='جنگل',
            ),
            Category(
                name='رودخونه',
            ),
        ]

        for category in categories:
            session.add(category)

        session.commit()

    def Test_list_category(self):
        with self.given(
            'List categories',
            '/apiv1/categories',
            'LIST'
        ):
            assert status == 200
            assert len(response.json) == 2
