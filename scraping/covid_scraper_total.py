# selenium imports
from selenium.webdriver.common.by import By # type of query for locating elements

from time import sleep # hacky, but sometimes the only option (i won't overdo it i swear)

class CovidScraperTotal():

    def __init__(self, dashboard):

        # where all the gathered data will be kept
        self.data = {
            'confirmed': None,
            'possible': None,
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

    def get_possible(self):

        # get number of possible cases and convert it to a numeric value
        self.data['possible'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[2]/margin-container/full-container/div/div[1]/div/div[2]"
            ).text.replace(".", "")
        )

        return self.data['possible']

    def get_recovered(self):

        # get number of recovered cases and convert it to a numeric value
        self.data['recovered'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[18]/margin-container/full-container/div/div[1]/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['recovered']

    def get_hospitalized(self):

        # get total number of hospitalized people and convert it to a number
        self.data['hospitalized'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[11]/margin-container/full-container/div/div/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['hospitalized']

    def get_interned(self):

        # get total number of interned people and convert it to a number
        self.data['interned'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[12]/margin-container/full-container/div/div/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['interned']

    def get_dead(self):

        # get total number of deaths and convert it to a number
        self.data['dead'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[13]/margin-container/full-container/div/div/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['dead']

    def get_all(self):

        self.get_hospitalized()
        self.get_interned()
        self.get_dead()
        self.get_confirmed()
        self.get_possible()
        self.get_recovered()

        return self.data