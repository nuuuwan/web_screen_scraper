import argparse
import os
import random
import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from utils import timex, twitter, www

from web_screen_scraper._utils import get_image_file, init_data_dir, log
from web_screen_scraper.CONFIG import CONFIG

DEFAULT_TIME_LOAD = 5
DEFAULT_WINDOW_WIDTH_HEIGHT = 3200, 1800


def open_browser():
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    return browser


def quit_browser(browser):
    browser.quit()


def get_raw_image(browser, name, url, window_width_height, time_load):
    raw_image_file = get_image_file(name, 'raw')
    if os.path.exists(raw_image_file):
        return raw_image_file

    log.info(f'Processing {name} ({url})')

    browser.get(url)
    window_width, window_height = window_width_height
    browser.set_window_size(window_width, window_height)

    imgs = browser.find_elements_by_id('ImageChart')
    if imgs:
        src = imgs[0].get_attribute('src')
        www.download_binary(src, raw_image_file)
        return raw_image_file

    time.sleep(time_load)
    browser.get_screenshot_as_file(raw_image_file)
    log.info(f'Saved raw screenshot to {raw_image_file}')

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
    tweet_text = f'''{header}

{footer}
Source: {url} ({date})'''

    twtr = twitter.Twitter.from_args()
    twtr.tweet(
        tweet_text=tweet_text,
        status_image_files=[cropped_image_file],
        update_user_profile=True,
    )


def run(browser, d):
    name = d['name']
    url = d['url']
    window_width_height = d.get(
        'window_width_height', DEFAULT_WINDOW_WIDTH_HEIGHT
    )
    time_load = d.get('time_load', DEFAULT_TIME_LOAD)

    raw_image_file = get_raw_image(
        browser, name, url, window_width_height, time_load
    )
    cropped_image_file = get_image_file(name, 'cropped')

    left_top = d.get('left_top', None)
    if left_top:
        width_height = d['width_height']
        get_cropped_image(name, raw_image_file, left_top, width_height)
    else:
        os.system(f'cp "{raw_image_file}" "{cropped_image_file}"')

    header = d['header']
    footer = d['footer']

    tweet(header, url, footer, cropped_image_file)


def run_all(freq):
    browser = open_browser()
    filtered_config = list(filter(lambda d: d['freq'] == freq, CONFIG))
            
    n_filtered_config = len(filtered_config)
    log.info(f'Found {n_filtered_config} config items with freq={freq}')


    for d in filtered_config:
        time_sleep = 60 * (1 + random.random())
        log.info(f'Sleeping for {time_sleep}s')
        time.sleep(time_sleep)
        try:
            run(browser, d)
        except Exception as e:
            log.error(str(e))
    quit_browser(browser)


def get_args_freq():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(
        'freq',
        help='Frequency of Cron',
        type=int,
        default=7,
    )
    args = parser.parse_args()
    return args.freq


if __name__ == '__main__':
    freq = get_args_freq()
    init_data_dir()
    run_all(freq)
