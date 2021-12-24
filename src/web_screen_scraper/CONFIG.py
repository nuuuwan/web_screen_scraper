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
    #     header='#COVIDI19SL Vaccination Dashboard by presidentsoffice.gov.lk',
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
]
