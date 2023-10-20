"""
Grabber runner.

Run it to collect pictures (after making settings in settings.py).
"""
from settings import PAGES, PATH, WORD
from yandexpics import YandexPictures

load_pics = YandexPictures(WORD, PAGES, PATH)
load_pics.do_search()
