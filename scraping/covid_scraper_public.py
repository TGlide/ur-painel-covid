from selenium.webdriver.common.by import By # type of query for locating elements

from covid_scraper_utils import change_to_right_subpanel

class CovidScraperPublic():

    def __init__(self, dashboard):

        self.data = {
            'hospitalized': None,
            'interned': None,
            'dead': None
        }

        self.dashboard = dashboard

    def get_hospitalized(self):

        # go to first subpanel
        change_to_right_subpanel(self.dashboard, 1)

        # get total number of hospitalized people in the public health system and convert it to a number
        self.data['hospitalized'] = int(
            self.dashboard.find_element(
                By.XPATH,
                "div[7]/margin-container/full-container/div/div/div/div[2]"
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
                "div[8]/margin-container/full-container/div/div/div/div[2]"
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
                "div[18]/margin-container/full-container/div/div/div/div[2]"
            ).text.replace(".", "").replace(",", "")
        )

        return self.data['dead']

    def get_all(self):

        self.get_hospitalized()
        self.get_interned()
        self.get_dead()

        return self.data