from django.shortcuts import render
from ..config import initilizationData

def getContextData():
    context = {
        'CountryName':initilizationData['country'],
        'navLogoImage':initilizationData['navLogoImage'],
        'defaultView':initilizationData['defaultView'],
        'TethysAppName':initilizationData['TethysAppName'],
        'AdminLevel':initilizationData['AdminLevel'],
        'regionOrCountryId':initilizationData['regionOrCountryId'],
        'TethysAPIAppName':initilizationData['TethysAPIAppName'],
        'DefaultPlotInfo':initilizationData['DefaultPlotInfo'],
        'MaskWMS':initilizationData['MaskWMS'],
        'ForceMaxZoomOut':initilizationData['ForceMaxZoomOut'],
    }
    return context

def Recent(request):
    """
    Controller for the app home page.
    """

    context = getContextData();
    return render(request, 'aqwatchhkh/recent_AirQualityWatch.html', context)


def Archive(request):
    """
    Controller for the app home page.
    """

    context = getContextData();


    return render(request, 'aqwatchhkh/archive_AirQualityWatch.html', context)


def Forecast(request):
    """
    Controller for the app home page.
    """
    context = getContextData();

    return render(request, 'aqwatchhkh/forecast_AirQualityWatch.html', context)
