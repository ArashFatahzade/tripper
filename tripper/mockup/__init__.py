from os.path import dirname, abspath, join
from random import random, randint, choice

from restfulpy.orm import DBSession
from sqlalchemy_media import StoreManager

from tripper.models import Place, PlaceImage, PlaceImageList, Category

MOCKUP_DIR = abspath(dirname(__file__))
IMAGE_PATH = join(MOCKUP_DIR, 'stuff')


def mockup():
    with StoreManager(DBSession):
        images = PlaceImageList([
            PlaceImage.create_from(f'{IMAGE_PATH}/1.jpeg'),
            PlaceImage.create_from(f'{IMAGE_PATH}/2.jpeg'),
        ])

        categories = [
            Category(
                name='جنگل',
            ),
            Category(
                name='رودخونه',
            ),
            Category(
                name='کوه',
            ),
            Category(
                name='مذهبی',
            ),
        ]

        for i in range(1000):
            place = Place(
                name=f'foo {i}',
                description=description,
                address=address,
                latitude=random() * 20 + 30,
                longitude=random() * 20 + 30,
                images=images,
                category=choice(categories),
            )
            DBSession.add(place)

        DBSession.commit()


address = '''
لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم
 از صنعت چاپ و با استفاده از طراحان.
 '''


description = '''
لورم ایپسوم متن ساختگی با
 تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها
 و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط
 فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی
 می باشد. کتابهای زیادی در شصت و سه درصد گذشته، حال و آینده شناخت فراوان
 جامعه و متخصصان را می طلبد تا با نرم افزارها شناخت بیشتری را برای طراحان
 رایانه ای علی الخصوص طراحان خلاقی و فرهنگ پیشرو در زبان فارسی ایجاد کرد.
 در این صورت می توان امید داشت که تمام و دشواری موجود در ارائه راهکارها
 و شرایط سخت تایپ به پایان رسد و زمان مورد نیاز شامل حروفچینی دستاوردهای 
اصلی و جوابگوی سوالات پیوسته اهل دنیای موجود طراحی اساسا مورد استفاده قرار گیرد. 
'''
