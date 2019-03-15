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
            image1 = PlaceImage.create_from(f'{IMAGE_PATH}/1.jpeg')
            image2 = PlaceImage.create_from(f'{IMAGE_PATH}/2.jpeg')

            jungle_category = Category(
                name='Jungle',
            )

            place1 = Place(
                name='foo',
                description='bar',
                address='a/b/c/d',
                latitude=0,
                longitude=0,
                images=PlaceImageList(),
                category=jungle_category,
            )
            place1.images.append(image1)
            place1.images.append(image2)
            session.add(place1)

            session.commit()

    def test_list_place(self):
        with self.given(
            'Get place',
            '/apiv1/places/id: 1',
            'GET'
        ):
            assert status == 200
            place = response.json
            assert place['id'] is not None
            assert place['name'] is not None
            assert place['description'] is not None
            assert place['address'] is not None
            assert place['images'] is not None
            assert place['latitude'] is not None
            assert place['longitude'] is not None
            assert place['category'] is not None

            when(
                'Place Not Found',
                url_parameters=dict(id=0),
            )
            assert status == 404
