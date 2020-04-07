# selenium imports
from selenium.webdriver.common.by import By # type of query for locating elements
from selenium.webdriver.support.ui import WebDriverWait # wait until condition is fullfiled
from selenium.webdriver.support import expected_conditions as EC # condition to be fullfiled
from selenium.webdriver.common.action_chains import ActionChains # perform user interaction actions
from selenium.webdriver.common.keys import Keys # common keys

from time import sleep # hacky, but sometimes the only option (i won't overdo it i swear)

class CovidScraperGeneralNumbers():


    def __init__(self, dashboard):

        # where all the gathered data will be kept
        self.data = {
            'confirmed': None,
            'possible': None,
            'recovered': None
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
            ).text.replace(".", "")
        )

        return self.data['recovered']

    def get_all(self):

        self.get_confirmed()
        self.get_possible()
        self.get_recovered()

        return self.data