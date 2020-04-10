#selenium imports
from selenium.webdriver.common.by import By # type of query for locating elements
from selenium.webdriver.support.ui import WebDriverWait # wait until condition is fullfiled
from selenium.webdriver.support import expected_conditions as EC # condition to be fullfiled

# custom imports
from covid_scraper_utils import dropdown_menu_set # toogle deaf/confirmed mode
from covid_scraper_utils import change_to_left_subpanel
# built-in
from time import sleep
import csv

class CovidScraperHood():

    def __init__(self, driver, navbar, dashboard, timeout=5):

        # where all the gathered data will be kept
        self.data = dict()
        '''
        'neighborhood_name' = {
            'confirmed': None,
            'dead': None,
            'recovered': None
        }
        '''

        self.driver = driver
        self.navbar = navbar
        self.dashboard = dashboard

        # number of seconds we sleep to wait for the panel to update
        self.timeout = timeout

        # path to access the list of neighborhoods
        self.hood_confirmed_list = "div[3]/margin-container/full-container/div/div[2]/nav/span"

        self.hood_dead_list = "div[5]/margin-container/full-container/div/div[2]/nav/span"

    def get_neighborhood_cases(self, hood_element):

        # to make sure we can parse the values properly
        convert_to_int = lambda str: int(str.replace(",", "").replace(".", "")) 

        # get contents out of the tag and feed it to self.data
        value, key = hood_element.text.split(" ", 1)

        # check if we need to create dictionary
        if( isinstance( self.data.get(key, None), dict ) ):
            self.data[key]['confirmed'] = convert_to_int(value)
        else:
            self.data[key] = { 'confirmed' : convert_to_int(value) }

        return self.data[key]['confirmed']

    def get_neighborhoods_cases(self):

        # check for confirmed cases
        dropdown_menu_set(self.driver, self.navbar, "Todos os confirmados")
        change_to_left_subpanel(self.dashboard, 1)

        # iterate over the neighborhood tags and gather data from each one
        for neighborhood in self.dashboard.find_elements(By.XPATH, self.hood_confirmed_list):

            self.get_neighborhood_cases(neighborhood)

        return self.data

    def get_neighborhood_deaths(self, hood_element):

        # to make sure we can parse the values properly
        convert_to_int = lambda str: int(str.replace(",", "").replace(".", "")) 

        # get contents out of the tag and feed it to self.data
        value, key = hood_element.text.split(" ", 1)

        # check if we need to create dictionary
        if( isinstance( self.data.get(key, None), dict ) ):
            self.data[key]['dead'] = convert_to_int(value)
        else:
            self.data[key] = { 'dead' : convert_to_int(value) }

        return self.data[key]['dead']

    def get_neighborhoods_deaths(self):

        # check for confirmed cases
        dropdown_menu_set(self.driver, self.navbar, "Todos os confirmados")
        change_to_left_subpanel(self.dashboard, 2)

        # iterate over the neighborhood tags and gather data from each one
        for neighborhood in self.dashboard.find_elements(By.XPATH, self.hood_dead_list):

            self.get_neighborhood_deaths(neighborhood)

        change_to_left_subpanel(self.dashboard, 1)

        return self.data

    def get_neighborhood_recovered(self, neighborhood_key):

        # get value in red panel
        value = int(self.dashboard.find_element(
                    By.XPATH,
                    "div[1]/margin-container/full-container/div/div/div/div[2]"
                ).text.replace(",", ""))

        if( isinstance( self.data.get(neighborhood_key, None), dict) ):
            self.data[neighborhood_key]['recovered'] = value
        else:
            self.data[neighborhood_key] = { 'recovered' : value }

        return self.data[neighborhood_key]['recovered']

    def get_neighborhoods_recovered(self):

        # check for recovered
        dropdown_menu_set(self.driver, self.navbar, "Recuperados")
        change_to_left_subpanel(self.dashboard, 1)

        # make sure panel is updated
        sleep(self.timeout)

        # iterate through neighborhoods and get death toll of each one
        for neighborhood in self.dashboard.find_elements(By.XPATH, self.hood_confirmed_list):

            # click neighborhood tile in the list
            neighborhood.click()

            # get name of the neighborhood
            neighborhood_name = neighborhood.text.split(" ", 1)[1]

            # wait for 1 second so that the panel is updated
            sleep(self.timeout)
            self.get_neighborhood_recovered(neighborhood_name)

        # got back to show confirmed cases     
        dropdown_menu_set(self.driver, self.navbar, "Todos os confirmados")

        # click once again on the last neighborhood so we go back seeing the total cases
        self.dashboard.find_element(By.XPATH, self.hood_confirmed_list + "[last()]").click()

        # wait again so we don't perform any actions without updating the panel
        sleep(self.timeout) 

        return self.data

    def to_csv(self, filename):

        with open(filename, "w") as f:
            fieldnames = ['neighborhood', 'confirmed', 'dead', 'recovered']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            # write header
            writer.writeheader()
            for neighborhood in self.data.keys():
                writer.writerow({
                    'neighborhood': neighborhood,
                    'confirmed': self.data[neighborhood]['confirmed'],
                    'dead': self.data[neighborhood]['dead'],
                    'recovered': self.data[neighborhood]['recovered']
                })

    def get_all(self):

        self.get_neighborhoods_cases()
        self.get_neighborhoods_deaths()
        self.get_neighborhoods_recovered()

        return self.data