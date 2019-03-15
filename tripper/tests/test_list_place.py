from os.path import dirname, abspath, join

from bddrest import response, status, when
from sqlalchemy_media import StoreManager

from tripper.models import Place, PlaceImage, PlaceImageList, Category

from .helpers import LocalApplicationTestCase


TEST_DIR = abspath(dirname(__file__))
IMAGE_PATH = join(TEST_DIR, 'stuff')


class TestPlace(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()
        with StoreManager(session):
            images = PlaceImageList([
                PlaceImage.create_from(f'{IMAGE_PATH}/1.jpeg'),
                PlaceImage.create_from(f'{IMAGE_PATH}/2.jpeg'),
            ])

            jungle_category = Category(
                name='Jungle',
            )

            place1 = Place(
                name='foo',
                description='bar',
                address='a/b/c/d',
                latitude=0,
                longitude=0,
                images=images,
                category=jungle_category,
            )
            session.add(place1)

            place2 = Place(
                name='foo',
                description='bar',
                address='a/b/c/d',
                latitude=1,
                longitude=1,
                category=jungle_category,
            )
            session.add(place2)

            place3 = Place(
                name='foo',
                description='bar',
                address='a/b/c/d',
                latitude=3,
                longitude=3,
                category=jungle_category,
            )
            session.add(place3)

            session.commit()

    def test_list_place(self):
        with self.given(
            'List places',
            '/apiv1/places',
            'LIST'
        ):
            assert status == 200
            assert len(response.json) == 3
            assert len(response.json[0]['images']) == 2

            when(
                'Filter',
                query=dict(latitude='>2'),
            )
            assert len(response.json) == 1

            when(
                'Sort',
                query=dict(sort='-latitude'),
            )
            assert response.json[0]['latitude'] > response.json[1]['latitude']
            assert response.json[1]['latitude'] > response.json[2]['latitude']

            when(
                'Paginate',
                query=dict(skip=0, take=2),
            )
            assert len(response.json) == 2
