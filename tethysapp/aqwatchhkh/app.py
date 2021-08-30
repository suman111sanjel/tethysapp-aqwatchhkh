from tethys_sdk.base import TethysAppBase, url_map_maker


class Aqwatchhkh(TethysAppBase):
    """
    Tethys app class for Aqwatchhkh.
    """

    name = 'Air Quality Watch - HKH'
    index = 'aqwatchhkh:recent'
    icon = 'aqwatchhkh/images/icon.gif'
    package = 'aqwatchhkh'
    root_url = 'aqwatchhkh'
    color = '#f39c12'
    description = ''
    tags = 'Air Quality Watch'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='recent',
                url='aqwatchhkh/recent',
                controller='aqwatchhkh.controllers.home.Recent'
            ), UrlMap(
                name='archive',
                url='aqwatchhkh/archive',
                controller='aqwatchhkh.controllers.home.Archive'
            ), UrlMap(
                name='forecast',
                url='aqwatchhkh/forecast',
                controller='aqwatchhkh.controllers.home.Forecast'
            ),
        )

        return url_maps
