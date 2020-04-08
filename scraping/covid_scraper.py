# selenium imports
from selenium import webdriver # webdriver for automated browser
from selenium.webdriver.firefox.options import Options # options for the browser
from selenium.webdriver.common.by import By # type of query for locating elements
from selenium.webdriver.support.ui import WebDriverWait # wait until condition is fullfiled
from selenium.webdriver.support import expected_conditions as EC # condition to be fullfiled

# custom classes imports
from covid_scraper_total import CovidScraperTotal
from covid_scraper_hood import CovidScraperHood
from covid_scraper_public import CovidScraperPublic
from covid_scraper_graph import CovidScraperGraph

# built-in imports
from datetime import datetime # datetime object
import json # for requests and pretty-printing results

class CovidScraper:

    def __init__(self, headless=True, timeout=300, binary_path="geckodriver"):

        # where all the data we gather will be kept
        self.data = {
            'total': None,
            'neighborhoods': None,
            'last_update': None,
            'public': None,
            'daily': None
        }

        # initialize the driver at the dashboard URL and switch its context to the dashboard's iframe
        self.driver = self._setup_driver(headless, timeout, binary_path)

        # get navbar
        self.navbar = self.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[@class='margin-container']/div[@class='full-container']/div")

        # get time of the last update (if it is in maintenance, None will be returned)
        self.data['last_update'] = self._page_status()

        # get main dashboard tag (so we don't need to search from root everytime)
        if( self.data['last_update'] ): self.dashboard = self.driver.find_element(By.XPATH, "//html/body/div/div/div[2]/div/div/div/margin-container/full-container")

        # classes which will help us gather the data we want
        self.total = CovidScraperTotal(self.dashboard)
        self.hoods = CovidScraperHood(self.driver, self.navbar, self.dashboard)
        self.public = CovidScraperPublic(self.dashboard)
        self.graph = CovidScraperGraph(self.dashboard)

    def _setup_driver(self, headless, timeout, binary_path):

        # set starting URL and if we will run headless or not
        options = Options()
        options.headless = headless
        options.add_argument("https://experience.arcgis.com/experience/38efc69787a346959c931568bd9e2cc4")

        # initialize browser
        driver = webdriver.Firefox(options = options, executable_path=binary_path)

        # tell the driver to wait if element being searched isn't found at first (default: 5 min)
        driver.implicitly_wait(timeout)

        # get iframe with all the data and switch to it
        iframe = WebDriverWait(driver, timeout).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe")) # get iframe
        )

        return driver

    def _page_status(self):

        # get text in navbar containing the time it was last updated
        last_update_str = self.navbar.find_element(By.XPATH, "div[2]/div[2]").text

        # check if page is under maintance right now
        if( last_update_str == None or "atualização" in  last_update_str):
            last_update = None   
        else:
            # if not, get the time of the last update
            last_update = datetime.strptime(last_update_str, "boletim de %d/%m/%Y %H:%M - SMS | IPP | COR")

        return last_update

    def get_all(self):

        print(self)
        self.data['public'] = self.public.get_all()
        print(self)
        self.data['total'] = self.total.get_all()
        print(self)
        self.data['daily'] = self.graph.get_all()
        print(self)
        self.data['neighborhoods'] = self.hoods.get_all()
        print(self)

    def __del__(self):

        # close driver
        self.driver.quit()

    def __repr__(self):

        string = json.dumps(self.data, sort_keys=True, indent=4, default=str)

        return string

# testting
if( __name__ == "__main__" ):
    scavanger = CovidScraper(headless=True)
    scavanger.get_all()
