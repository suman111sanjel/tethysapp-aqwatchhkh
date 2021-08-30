# from t
from tethysapp.aqwatchhkh.app import Aqwatchhkh

TethysAppName = Aqwatchhkh.package

AllRegion={0:'HKH',
           1:'AFGHANISTAN',
           4:'BANGLADESH',
           7:'BHUTAN',
           8:'CHINA',
           3:'INDIA',
           6:'MYANMAR',
           5:'NEPAL',
           2:'PAKISTAN'}

initilizationData = {
    'country': 'HKH',
    'navLogoImage': '/static/' + TethysAppName + '/images/nologo.png',
    'defaultView': '''
    {
        center: ol.proj.transform([84.87911057853935, 28.33233423278891], 'EPSG:4326', 'EPSG:3857'),
        zoom: 5.1069803526158335,
       extent: [6702855.884774126, 1769255.1930753174, 12194542.852403797, 4812621.833531793]
    }
    ''',
    'DefaultPlotInfo':'''
    {
        colorScheme: 'jet',
        BBOX: [60, 15, 110, 40],
        tickSpan: 10,
        Resolution: 600,
        width: 12,
        height: 9
    }
    ''',
    'TethysAppName': TethysAppName,
    'AdminLevel': 'l2Jumla',
    'regionOrCountryId': 0,
    'TethysAPIAppName':'aqwatchapi',
    'MaskWMS': 'false',
    'ForceMaxZoomOut':'true'
}