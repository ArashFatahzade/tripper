import sys
from time import sleep
from os.path import basename

import json
from requests import request, RequestException
from easycli import SubCommand, Argument
from restfulpy.orm import DBSession

from ..models import RawPlace


HEADERS = {
    'accept-encoding': 'gzip, deflate, br',
    'x-requested-with': 'XMLHttpRequest',
}

class TryAgain(Exception):
    pass


class KojaroLuncher(SubCommand):
    __completion__ = True
    __command__ = 'kojaro'
    __arguments__ = [
        Argument(
            '-V', '--version',
            action='store_true',
            help='Show application version',
        ),
    ]

    def __call__(self, args):
        index = DBSession.query(RawPlace).count() // 20 + 1
        while True:
            try:
                print(index)
                self.get_page(index)
                index += 1
            except StopIteration:
                break
            except TryAgain:
                print(f'Error on getting {index}')
            finally:
                sleep(1)

    def get_page(self, index):
        try:
            response = request(
                method='POST',
                url='https://www.kojaro.com/attraction/filter/iran-3-co/',
                data=dict(params=f'page/{index}/'),
                headers=HEADERS,
            )
        except RequestException:
            raise TryAgain()

        if response.status_code != 200:
            raise TryAgain()

        response = json.loads(response.text)
        if not response['isSucceed']:
           raise StopIteration()

        places = response['result']['directories']
        for place in places:
            raw_place = RawPlace(data=place)
            DBSession.add(raw_place)

        DBSession.commit()

