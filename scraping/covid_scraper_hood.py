from selenium.webdriver.common.by import By # type of query for locating elements
from selenium.webdriver.support.ui import WebDriverWait # wait until condition is fullfiled
from selenium.webdriver.support import expected_conditions as EC # condition to be fullfiled

class CovidScraperHood():

    def __init__(self, dashboard):

        # where all the gathered data will be kept
        self.data = {
        }

        self.dashboard = dashboard

    def get_neighborhood(self, hood_element):

        # to make sure we can parse the values properly
        convert_to_int = lambda str: int(str.replace(",", "").replace(".", "")) 

        # get contents out of the tag and feed it to self.data
        value, key = hood_element.text.split(" ", 1)

        self.data[key] = convert_to_int(value)

        return self.data[key]

    def get_neighborhoods(self):

        # path to access the list of neighborhoods
        hood_list = "div[3]/margin-container/full-container/div/div[2]/nav/span"

        # iterate over the neighborhood tags and gather data from each one
        for neighborhood in self.dashboard.find_elements(By.XPATH, hood_list):

            self.get_neighborhood(neighborhood)

        return self.data

    def get_all(self):

        return self.get_neighborhoods()