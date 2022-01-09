"""Utils."""
import logging
import os

from utils import timex

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('web_screen_scraper')


def get_data_dir():
    date_id = timex.get_date_id()
    return f'/tmp/wss.{date_id}'


def init_data_dir():
    data_dir = get_data_dir()
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
        log.info(f'Created {data_dir}')


def get_image_file(name, suffix):
    return os.path.join(get_data_dir(), f'{name}.{suffix}.png')
