# selenium imports
from selenium.webdriver.common.by import By # type of query for locating elements

# custom imports
from covid_scraper_utils import change_to_right_subpanel

# built-in imports
from time import sleep # hacky, but sometimes the only option (i won't overdo it i swear)

class CovidScraperCurrent():

    def __init__(self, dashboard):

        # where all the gathered data will be kept
        self.data = {
            'confirmed': None,
            'recovered': None,
            'sus': {
                'hospitalized': None,
                'uti': None,
                'dead': None
            },
            'municipal': {
                'hospitalized': None,
                'uti': None,
                'dead': None
            }
        }

        self.dashboard = dashboard

    def get_confirmed(self):

        # get number of confirmed cases and convert it to a numeric type
        self.data['confirmed'] = int(
                self.dashboard.find_element(
                    By.XPATH,
                    "div[1]/margin-container/full-container/div/div/div/div[2]"
                ).text.replace(",", "")
            )

        return self.data['confirmed']

    def get_recovered(self):

        # get number of recovered cases and convert it to a numeric value
        self.data['recovered'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[2]/margin-container/full-container/div/div[1]/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['recovered']


    def get_municipal_hospitalized(self):

        # go to first subpanel
        change_to_right_subpanel(self.dashboard, 1)

        # get total number of hospitalized people in the public health system and convert it to a number
        self.data['municipal']['hospitalized'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[9]/margin-container/full-container/div/div/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['municipal']['hospitalized']

    def get_municipal_uti(self):

        # go to first subpanel
        change_to_right_subpanel(self.dashboard, 1)

        # get total number of people in uti and convert it to a number
        self.data['municipal']['uti'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[10]/margin-container/full-container/div/div/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['municipal']['uti']

    def get_municipal_dead(self):

        # go to first subpanel
        change_to_right_subpanel(self.dashboard, 1)

        # get total number of deaths and convert it to a number
        self.data['municipal']['dead'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[20]/margin-container/full-container/div/div/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['municipal']['dead']

    def get_sus_hospitalized(self):

        # go to first subpanel
        change_to_right_subpanel(self.dashboard, 1)

        # get total number of hospitalized people and convert it to a number
        self.data['sus']['hospitalized'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[12]/margin-container/full-container/div/div/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['sus']['hospitalized']

    def get_sus_uti(self):

        # go to first subpanel
        change_to_right_subpanel(self.dashboard, 1)

        # get total number of people in UTI and convert it to a number
        self.data['sus']['uti'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[13]/margin-container/full-container/div/div/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['sus']['uti']

    def get_sus_dead(self):

        # get total number of deaths and convert it to a number
        self.data['sus']['dead'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[21]/margin-container/full-container/div/div/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['sus']['dead']

    def get_all(self):

        #self.get_lethality()

        # total
        self.get_confirmed()
        self.get_recovered()

        # total at municipal health system
        self.get_municipal_hospitalized()
        self.get_municipal_uti()
        self.get_municipal_dead()

        # total at sus
        self.get_sus_hospitalized()
        self.get_sus_uti()
        self.get_sus_dead()

        return self.data