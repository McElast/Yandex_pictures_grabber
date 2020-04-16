import requests
from bs4 import BeautifulSoup
import json
import os
import winsound

# --------- SETTINGS --------------
WORD = 'космос'
PAGES = 3
PATH = 'D:/downs/'
###################################


class YandexPictures:
    def __init__(self, search, num_pages, path, sounds=True):
        self.search = search
        self.num_pages = num_pages
        self.path = path
        self.pics_divs = []
        self.k = 0
        self.item = None
        self.clean = None
        self.sounds = sounds

    def _print_ok(self):
        print(f'page {self.k} - {self.pics_divs.index(self.item)} OK')

    def _look_save_pics(self):
        try:
            pica = requests.get(self.clean, timeout=5)
        except Exception as e:
            if self.sounds:
                winsound.Beep(500, 400)
            print('----ERROR---', self.clean)
            return
        if pica.status_code == 200:
            pica = pica.content
            self.clean = self._clear_url(self.clean)
            with open(f'{PATH}{self.search}/{self.clean[-22:]}', 'wb') as p:
                p.write(pica)
            self._print_ok()

    @staticmethod
    def _clear_url(uncleaned_url):
        bad_symbols = '/?:*"<>|\\'
        for sym in uncleaned_url:
            if sym in bad_symbols:
                uncleaned_url = uncleaned_url.replace(sym, '')
        return uncleaned_url

    def do_search(self):
        sess = requests.Session()
        sess.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                           'like Gecko) Chrome/74.0.3729.169 Safari/537.36'})
        for self.k in range(self.num_pages):
            link = f'https://yandex.ru/images/search?text={self.search}&isize=eq&iw=1920&ih=1080&p={self.k}'
            a = sess.get(link)
            soup = BeautifulSoup(a.text, 'html.parser')
            self.pics_divs = soup.find_all('div', class_='serp-item_type_search')
            try:
                os.mkdir(PATH + self.search)
            except FileExistsError:
                pass
            for self.item in self.pics_divs:
                json_data = json.loads(self.item.get('data-bem'))
                try:
                    self.clean = json_data['serp-item']['preview'][0]['url']
                except KeyError:
                    continue
                if self.clean[-3:] in ['jpg', 'png', 'peg', 'gif', 'svg', 'ebp']:
                    self._look_save_pics()
                else:
                    try:
                        self.clean = json_data['serp-item']['preview'][0]['origin']['url']
                    except KeyError:
                        continue
                    if self.clean[-3:] in ['jpg', 'png', 'peg', 'gif', 'svg', 'ebp']:
                        self._look_save_pics()

        if self.sounds:
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)


load_pics = YandexPictures(WORD, PAGES, PATH)
load_pics.do_search()
