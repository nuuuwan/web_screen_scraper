import os

from utils import timex

CONFIG = [
    dict(
        name='cbsl-gov-lk-economy-snapshot',
        url='https://www.cbsl.gov.lk/en/sri-lanka-economy-snapshot',
        left_top=[1020, 280],
        width_height=[860, 1040],
        header='#SriLanka #Economy Snapshot by @CBSL',
        footer='#lka',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='statistics-gov-lk-figures',
        url='http://www.statistics.gov.lk',
        left_top=[1700, 160],
        width_height=[460, 330],
        header='#SriLanka in Figures',
        footer='#lka',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='icc-team-rankings-test',
        url='https://www.icc-cricket.com/rankings/mens/team-rankings/test',
        time_load=10,
        left_top=[1050, 780],
        width_height=[1150, 530],
        header='Men\'s Test #Cricket - Team Rankings (@ICC)',
        footer='',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='tradingeconomics-lk-foreign-exchange-reserves',
        url='https://tradingeconomics.com/sri-lanka/foreign-exchange-reserves',
        header='#SriLanka Foreign Exchange Reserves',
        footer='@tEconomics @CBSL #lka #ForEx',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='tradingeconomics-lk-tourist-arrivals',
        url='https://tradingeconomics.com/sri-lanka/tourist-arrivals',
        header='#SriLanka Tourist Arrivals',
        footer='@tEconomics @TourismLK #lka',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='tradingeconomics-lk-gdp-growth-annual',
        url='https://tradingeconomics.com/sri-lanka/gdp-growth-annual',
        header='#SriLanka GDP Annual Growth Rate',
        footer='@tEconomics statistics.gov.lk #lka',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='tradingeconomics-lk-inflation-cpi',
        url='https://tradingeconomics.com/sri-lanka/inflation-cpi',
        header='#SriLanka Inflation Rate',
        footer='@tEconomics @CBSL #lka',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='tradingeconomics-lk-foreign-direct-investment',
        url='https://tradingeconomics.com/sri-lanka/foreign-direct-investment',
        header='#SriLanka Foreign Direct Investment'
        + ' - Net Inflows (USD Million)',
        footer='@tEconomics @CBSL #lka',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='tradingeconomics-lk-remittances',
        url='https://tradingeconomics.com/sri-lanka/remittances',
        header='#SriLanka Remittances (USD Million)',
        footer='@tEconomics @CBSL #lka',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='tradingeconomics-lk-exports',
        url='https://tradingeconomics.com/sri-lanka/exports',
        header='#SriLanka Exports (USD Million)',
        footer='@tEconomics @CBSL #lka',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='tradingeconomics-lk-imports',
        url='https://tradingeconomics.com/sri-lanka/imports',
        header='#SriLanka Imports (USD Million)',
        footer='@tEconomics @CBSL #lka',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='tradingeconomics-lk-tourism-revenues',
        url='https://tradingeconomics.com/sri-lanka/tourism-revenues',
        header='#SriLanka Tourism Revenues (USD Million)',
        footer='@tEconomics @CBSL #lka',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='tradingeconomics-lk-gdp-per-capita-ppp',
        url='https://tradingeconomics.com/sri-lanka/gdp-per-capita-ppp',
        header='#SriLanka GDP per capita PPP (USD)',
        footer='@tEconomics @WorldBank #lka',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='tradingeconomics-lk-youth-unemployment-rate',
        url='https://tradingeconomics.com/sri-lanka/youth-unemployment-rate',
        header='#SriLanka Youth Unemployment Rate',
        footer='@tEconomics statistics.gov.lk #lka',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='tradingeconomics-lk-food-inflation',
        url='https://tradingeconomics.com/sri-lanka/food-inflation',
        header='#SriLanka Food Inflation (YoY)',
        footer='@tEconomics statistics.gov.lk #lka',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='tradingeconomics-lk-exports-by-country',
        url='https://tradingeconomics.com/sri-lanka/exports-by-country',
        header='#SriLanka  Exports By Country',
        footer='@tEconomics @UNTradeStats #lka',
        left_top=[1030, 220],
        width_height=[770, 370],
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='tradingeconomics-lk-imports-by-country',
        url='https://tradingeconomics.com/sri-lanka/imports-by-country',
        header='#SriLanka  Imports By Country',
        footer='@tEconomics @UNTradeStats #lka',
        left_top=[1030, 220],
        width_height=[770, 370],
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='tradingeconomics-lk-car-registrations',
        url='https://tradingeconomics.com/sri-lanka/car-registrations',
        header='#SriLanka Car Registrations',
        footer='@tEconomics @CBSL #lka',
        freq=timex.SECONDS_IN.WEEK,
    ),
    dict(
        name='ventusky-lk-rain-3h',
        url='https://www.ventusky.com/?p=8.41;80.71;6&l=rain-3h',
        header='#SriLanka Weather via @VentuskyCom',
        footer='#lka',
        freq=timex.SECONDS_IN.HOUR * 3,
        window_width_height=[1600, 900],
    ),
    dict(
        name='google-maps-colombo-traffic',
        url=os.path.join(
            'https://www.google.com',
            'maps/@6.9157334,79.8575813,14.41z/data=!5m1!1e1',
        ),
        window_width_height=[2000, 2000],
        left_top=[700, 60],
        width_height=[1200, 1675],
        header='#Colombo Traffic via @GoogleMaps',
        footer='#SriLanka #lka',
        freq=timex.SECONDS_IN.HOUR * 3,
    ),
    dict(
        name='google-news-lk',
        url=os.path.join(
            'https://www.google.com/search?q=Sri+Lanka&tbm=nws&tbs=qdr:d',
        ),
        window_width_height=[900, 1500],
        left_top=[100, 170],
        width_height=[900 - 100, 1500 - 170 - 370],
        header='#SriLanka on @GoogleNews',
        footer='#lka',
        freq=timex.SECONDS_IN.HOUR * 3,
    ),
]
