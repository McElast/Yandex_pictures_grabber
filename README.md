Download yandex pictures (in python)

----- ENGLISH ----- 

Needed libraries: Beautiful soup, requests.

1.	HOW TO START 

yandexpics.py - open it and add settings: 

WORD - type any search query for pictures you need 

PATH - path for saving photos 

PAGES - how many pages to load (1 page = 30 photos)

Then just run script and get them all. 

2. Additions 

You can change User-Agent if you need here (sess.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}))


You can turn off sounds (errors and finish) by setting sounds=False


To change pics size (by default it equals 1920х1080), edit field: link = f'https://yandex.ru/images/search?text={self.search}&isize=eq&iw=1920&ih=1080&p={self.k}' 

Good Luck.

------ Русский ------ 

Скрипт качает картинки с Яндекс.Картинок Написано на python (вам потребуется интерпретатор - качается с оф. сайта) 

Также, нужно установить библиотеки: Beautiful soup, requests.

1.	Как запустить 

yandexpics.py - откройте этот файл и сделайте настройки: 

WORD - здесь пишем, что нужно найти 

PATH - тут указываем путь к папке будущих картинок 

PAGES - говорим скрипту, сколько страниц ему пролистывать (на одной - 30 фоток)


Потом запускаете скрипт и ждете.

2.	Дополнения 

Добавлены звуки (при ошибке и при завершении работы скрипта). Если напрягают - отключите (sounds=False).


Можно менять User-Agent на другой, если нужно. Вот строка: sess.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})


Для изменения размера загружаемых картинок править строку: link = f'https://yandex.ru/images/search?text={self.search}&isize=eq&iw=1920&ih=1080&p={self.k}' 

По умолчанию идет размер 1920х1080

Успехов!

