import os

CONFIG = [
    dict(
        name='cbsl-gov-lk-economy-snapshot',
        url='https://www.cbsl.gov.lk/en/sri-lanka-economy-snapshot',
        left_top=[1020, 280],
        width_height=[860, 1040],
        header='#SriLanka #Economy Snapshot by @CBSL',
        footer='#lka',
    ),
    # dict(
    #     name='presidentsoffice-gov-lk-vaccination-dashboard',
    #     url=os.path.join(
    #         'https://www.presidentsoffice.gov.lk/index.php',
    #         'vaccination-dashboard/',
    #     ),
    #     window_width_height=[3200, 2700],
    #     time_load=30,
    #     left_top=[60, 200],
    #     width_height=[3140, 1580],
    #     header='#COVID19SL Vaccination Dashboard by presidentsoffice.gov.lk',
    #     footer='#SriLanka  #lka #COVID19 #Vaccinated',
    # ),
    dict(
        name='statistics-gov-lk-figures',
        url='http://www.statistics.gov.lk',
        left_top=[1700, 160],
        width_height=[460, 330],
        header='#SriLanka in Figures',
        footer='#lka',
    ),
    dict(
        name='icc-team-rankings-test',
        url='https://www.icc-cricket.com/rankings/mens/team-rankings/test',
        time_load=10,
        left_top=[1050, 780],
        width_height=[1150, 530],
        header='Men\'s Test #Cricket - Team Rankings (@ICC)',
        footer='',
    ),
    dict(
        name='gmaps-colombo-traffic',
        url=os.path.join(
            'https://www.google.com',
            'maps/@6.9066389,79.8601593,13z/data=!5m1!1e1',
        ),
        window_width_height=[2000, 900],
        left_top=[700, 60],
        width_height=[1200, 675],
        header='#Colombo Traffic (@GoogleMaps)',
        footer='#SriLanka #lka',
    ),
]
