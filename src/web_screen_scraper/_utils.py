"""Utils."""
import logging
import os

from utils import timex

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('web_screen_scraper')


def get_data_dir():
    date_id = timex.get_date_id()
    return f'/tmp/wss.{date_id}'


def get_image_file(name, suffix):
    return os.path.join(get_data_dir(), f'{name}.{suffix}.png')
