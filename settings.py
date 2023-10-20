"""Grabber settings."""
import os

from fake_useragent import FakeUserAgent, UserAgent

# Can be changed for your needs
WORD: str = 'Pacific Ocean'
"""Search request for pictures."""

PAGES: int = 3
"""How many pages to scrap (about 30 pictures per page)."""

PATH: str = os.path.abspath(os.getcwd())
"""
Path on your PC for saving downloaded pictures.

By default - current working directory.
"""

# Other settings
fake_user_agent: FakeUserAgent = UserAgent()
"""Fake useragent for imitating browser."""
fake_user_agent_chrome: str = fake_user_agent.chrome
"""Chrome fake useragent."""

picture_formats: list = ['jpg', 'png', 'peg', 'gif', 'svg', 'ebp']
"""Allowed formats for needed pictures."""

search_link: str = f'https://yandex.ru/images/search?text={WORD}&isize=eq&iw=1920&ih=1080&p='
"""Yandex search link. Don't change."""

bad_symbols: str = '/?:*"<>|\\'
"""Symbols to exclude from picture name while saving."""
