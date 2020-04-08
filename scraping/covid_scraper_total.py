# selenium imports
from selenium.webdriver.common.by import By # type of query for locating elements

# custom imports
from covid_scraper_utils import change_to_right_subpanel

# built-in imports
from time import sleep # hacky, but sometimes the only option (i won't overdo it i swear)

class CovidScraperTotal():

    def __init__(self, dashboard):

        # where all the gathered data will be kept
        self.data = {
            'confirmed': None,
            'recovered': None,
            'hospitalized': None,
            'interned': None,
            'dead': None
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
    '''
    def get_lethality(self):

        # get number of possible cases and convert it to a numeric value
        self.data['lethality'] = float(
            self.dashboard.find_element(
                By.XPATH,
                "div[16]/margin-container/full-container/div/div[1]/div/div[2]"
            ).text.replace("%", "")
        )/100

        return self.data['lethality']
    '''
    def get_recovered(self):

        # get number of recovered cases and convert it to a numeric value
        self.data['recovered'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[2]/margin-container/full-container/div/div[1]/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['recovered']

    def get_hospitalized(self):

        # go to first subpanel
        change_to_right_subpanel(self.dashboard, 1)

        # get total number of hospitalized people and convert it to a number
        self.data['hospitalized'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[11]/margin-container/full-container/div/div/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['hospitalized']

    def get_interned(self):

        # go to first subpanel
        change_to_right_subpanel(self.dashboard, 1)

        # get total number of interned people and convert it to a number
        self.data['interned'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[12]/margin-container/full-container/div/div/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['interned']

    def get_dead(self):

        # go to first subpanel
        change_to_right_subpanel(self.dashboard, 1)

        # get total number of deaths and convert it to a number
        self.data['dead'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[20]/margin-container/full-container/div/div/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['dead']

    def get_all(self):

        #self.get_lethality()
        self.get_confirmed()
        self.get_recovered()
        self.get_hospitalized()
        self.get_interned()
        self.get_dead()

        return self.data