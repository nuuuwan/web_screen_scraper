import math
import random

from geo import geodata
from gig import ents
from PIL import Image
from utils import twitter, www

from web_screen_scraper._utils import get_image_file, init_data_dir, log

TIME_LOAD = 5
MIN_FILE_SIZE = 10_000
MAX_N_RETRY = 20

MIN_LAT = 5.923389
MAX_LAT = 9.835556
MIN_LNG = 79.516667
MAX_LNG = 81.879167
LAT_SPAN = MAX_LAT - MIN_LAT
LNG_SPAN = MAX_LNG - MIN_LNG
ZOOM = 15
DIM_WIDTH = 3
DIM_HEIGHT = 2


def latlng_to_xy(latlng):
    lat, lng = latlng
    x = math.floor(((lng + 180) / 360) * math.pow(2, ZOOM))
    y = math.floor(
        (
            (
                1
                - math.log(
                    math.tan((lat * math.pi) / 180)
                    + 1 / math.cos((lat * math.pi) / 180)
                )
                / math.pi
            )
            / 2
        )
        * math.pow(2, ZOOM)
    )
    return [x, y]


def get_map_url(xy):
    x, y = xy
    return f'https://tile.openstreetmap.org/{ZOOM}/{x}/{y}.png'


def get_random_latlng_nocheck():
    lat = MIN_LAT + LAT_SPAN * random.random()
    lng = MIN_LNG + LNG_SPAN * random.random()
    return [lat, lng]


def get_random_latlng():
    i_retry = 0
    while i_retry < MAX_N_RETRY:
        latlng = get_random_latlng_nocheck()
        regions = geodata.get_latlng_regions(latlng)
        gnd_id = regions.get('gnd')
        if gnd_id:
            return latlng, gnd_id
        i_retry += 1
    return None


def get_raw_image(latlng, gnd_id):
    xy = latlng_to_xy(latlng)
    x, y = xy

    raw_file_list = []
    for ix in range(0, DIM_WIDTH):
        dx = ix - (int)(DIM_WIDTH / 2)
        x1 = x + dx
        for iy in range(0, DIM_HEIGHT):
            dy = iy - (int)(DIM_HEIGHT / 2)
            y1 = y + dy
            url = get_map_url([x1, y1])
            raw_file = get_image_file(
                f'openstreetmap-single-z{ZOOM}-x{x1}.y{y1}', 'raw'
            )
            www.download_binary(url, raw_file)
            raw_file_list.append(raw_file)

    im0 = Image.open(raw_file_list[0])
    (width, height) = im0.size
    combined_im = Image.new('RGB', (width * DIM_WIDTH, height * DIM_HEIGHT))
    i = 0
    for ix in range(0, DIM_WIDTH):
        for iy in range(0, DIM_HEIGHT):
            im = Image.open(raw_file_list[i])
            i += 1
            combined_im.paste(
                im=im,
                box=(
                    width * ix,
                    height * iy,
                ),
            )

    lat, lng = latlng
    combined_raw_image_file = get_image_file(
        f'openstreetmap-{gnd_id}-z{ZOOM}'
        + f'-latlng{lat:.4f}N.{lng:.4f}E-{DIM_WIDTH}x{DIM_HEIGHT}',
        'raw',
    )
    combined_im.save(combined_raw_image_file)
    log.info(f'Saved {combined_raw_image_file}')
    return combined_raw_image_file


def run():
    latlng, gnd_id = get_random_latlng()
    if not latlng:
        return None
    raw_image_file = get_raw_image(latlng, gnd_id)

    gnd = ents.get_entity(gnd_id)
    gnd_name = gnd['name']
    lat, lng = latlng
    openstreetmap_url = (
        f'https://www.openstreetmap.org/#map={ZOOM}/{lat}/{lng}'
    )

    tweet_text = f'''{gnd_name} ({gnd_id})

Source: @openstreetmap ({openstreetmap_url})

#RandomGND #GramaNiladhariDivision #SriLanka'''

    twtr = twitter.Twitter.from_args()
    twtr.tweet(
        tweet_text=tweet_text,
        status_image_files=[raw_image_file],
        update_user_profile=True,
    )


if __name__ == '__main__':
    init_data_dir()
    run()
