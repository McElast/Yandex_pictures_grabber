"""Grabbing logic."""
import json
import logging
import os
from http import HTTPStatus

import requests
from bs4 import BeautifulSoup, ResultSet

from settings import bad_symbols, fake_user_agent_chrome, PAGES, PATH, picture_formats, search_link, WORD

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class YandexPictures:
    """Class for downloading pictures from Yandex."""

    def __init__(self, search: str = WORD, num_pages: int = PAGES, path: str = PATH) -> None:
        """Grabber initializer."""
        self.search: str = search
        self.num_pages: int = num_pages
        self.path: str = path

    @staticmethod
    def _print_ok(current_page: int, picture_index: int) -> None:
        """Logging success if downloaded picture."""
        logger.info(f'page {current_page} - {picture_index} OK')

    def _look_save_pics(self, image_url: str, page_num: int, image_num: int) -> None:
        """Find and save picture."""
        try:
            picture: requests.Response = requests.get(image_url, timeout=5)
        except requests.exceptions.ConnectionError:
            logger.warning(f'----ERROR--- connection: {image_url}')
            return

        if picture.status_code != HTTPStatus.OK:
            logger.warning(f'----ERROR--- status code: {picture.status_code}')
            return

        image_name: str = self._clear_url(image_url)

        with open(f'{PATH}/{self.search}/{image_name[-22:]}', 'wb') as picture_file:
            picture_file.write(picture.content)

        self._print_ok(page_num, image_num)

    @staticmethod
    def _clear_url(uncleaned_url: str) -> str:
        """Getting name for picture from address."""
        for symbol in uncleaned_url:
            if symbol in bad_symbols:
                uncleaned_url = uncleaned_url.replace(symbol, '')

        return uncleaned_url

    @staticmethod
    def _check_picture_url_correct(json_data: dict, origin: bool = False) -> str | None:
        try:
            if origin:
                return json_data['serp-item']['preview'][0]['origin']['url']
            return json_data['serp-item']['preview'][0]['url']
        except KeyError:
            return ''

    def do_search(self) -> None:
        """Iterating over pages and collecting images."""
        session: requests.Session = requests.Session()
        session.headers.update({'User-Agent': fake_user_agent_chrome})

        for page in range(self.num_pages):
            link: str = f'{search_link}{page}'
            current_page: int = page + 1
            response: requests.Response = session.get(link)
            soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
            print(222, soup.text)
            pictures_divs: ResultSet = soup.find_all('div', class_='serp-item_type_search')

            try:
                os.mkdir(f'{PATH}/{self.search}')
            except FileExistsError:
                logger.warning(f'Dir {PATH}/{self.search} already exists. Skipping creating...')

            for image_num, image in enumerate(pictures_divs):
                json_data: dict = json.loads(image.get('data-bem'))
                picture_url: str = self._check_picture_url_correct(json_data)

                if picture_url[-3:] not in picture_formats:
                    picture_url = self._check_picture_url_correct(json_data, origin=True)

                if picture_url:
                    self._look_save_pics(picture_url, current_page, image_num + 1)
