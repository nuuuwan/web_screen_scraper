import os
import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from utils import timex, twitter

from web_screen_scraper._utils import log
from web_screen_scraper.CONFIG import CONFIG

DEFAULT_TIME_LOAD = 5
DEFAULT_WINDOW_WIDTH_HEIGHT = 3200, 1800


def get_data_dir():
    date_id = timex.get_date_id()
    return f'/tmp/wss.{date_id}'


def init():
    data_dir = get_data_dir()
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
        log.info(f'Created {data_dir}')


def get_image_file(name, suffix):
    return os.path.join(get_data_dir(), f'{name}.{suffix}.png')


def get_raw_image(name, url, window_width_height, time_load):
    raw_image_file = get_image_file(name, 'raw')
    if os.path.exists(raw_image_file):
        return raw_image_file

    log.info(f'Processing {name} ({url})')

    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)
    driver.get(url)
    window_width, window_height = window_width_height
    driver.set_window_size(window_width, window_height)

    time.sleep(time_load)
    driver.get_screenshot_as_file(raw_image_file)
    log.info(f'Saved raw screenshot to {raw_image_file}')
    driver.quit()

    return raw_image_file


def get_cropped_image(
    name, raw_image_file, left_top, width_height, force=True
):
    cropped_image_file = get_image_file(name, 'cropped')
    if not force:
        if os.path.exists(cropped_image_file):
            return cropped_image_file

    im = Image.open(raw_image_file)
    left, top = left_top
    width, height = width_height
    right, bottom = left + width, top + height

    im_cropped = im.crop((left, top, right, bottom))

    im_cropped.save(cropped_image_file)
    log.info(f'Saved cropped image to {cropped_image_file}')
    return cropped_image_file


def tweet(header, url, footer, cropped_image_file):
    date = timex.get_date()
    tweet_text = f'''{header} ({date})

{footer}

Source: {url}'''

    twtr = twitter.Twitter.from_args()
    twtr.tweet(
        tweet_text=tweet_text,
        status_image_files=[cropped_image_file],
        update_user_profile=True,
    )


def run(d):
    name = d['name']
    url = d['url']
    window_width_height = d.get(
        'window_width_height', DEFAULT_WINDOW_WIDTH_HEIGHT
    )
    time_load = d.get('time_load', DEFAULT_TIME_LOAD)

    raw_image_file = get_raw_image(name, url, window_width_height, time_load)
    left_top = d['left_top']
    width_height = d['width_height']
    cropped_image_file = get_cropped_image(
        name, raw_image_file, left_top, width_height
    )
    header = d['header']
    footer = d['footer']

    tweet(header, url, footer, cropped_image_file)


def run_all():
    for d in CONFIG:
        run(d)


if __name__ == '__main__':
    init()
    run_all()
