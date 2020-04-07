# selenium imports
from selenium import webdriver # webdriver for automated browser
from selenium.webdriver.firefox.options import Options # options for the browser
from selenium.webdriver.common.by import By # type of query for locating elements
from selenium.webdriver.support.ui import WebDriverWait # wait until condition is fullfiled
from selenium.webdriver.support import expected_conditions as EC # condition to be fullfiled

# custom classes imports
from covid_scraper_general_numbers import CovidScraperGeneralNumbers
from covid_scraper_hood import CovidScraperHood

# built-in imports
from datetime import datetime # datetime object
import json # for requests and pretty-printing results

class CovidScraper:

    def __init__(self, headless=True, timeout=300, binary_path="geckodriver"):

        # where all the data we gather will be kept
        self.data = {
            'total': None,
            'neighborhoods': None
        }

        # initialize the driver at the dashboard URL and switch its context to the dashboard's iframe
        self.driver = self._setup_driver(headless, timeout, binary_path)

        # get navbar
        self.navbar = self.driver.find_element(By.XPATH, "//body/div/div/div[1]/div[@class='margin-container']/div[@class='full-container']/div")

        # get time of the last update (if it is in maintenance, None will be returned)
        self.last_update = self._page_status()

        # get main dashboard tag (so we don't need to search from root everytime)
        if( self.last_update ): self.dashboard = self.driver.find_element(By.XPATH, "//html/body/div/div/div[2]/div/div/div/margin-container/full-container")

        # classes which will help us gather the data we want
        self.general_numbers = CovidScraperGeneralNumbers(self.dashboard)
        self.hoods = CovidScraperHood(self.driver, self.navbar, self.dashboard)

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

        self.data['total'] = self.general_numbers.get_all()
        self.data['neighborhoods'] = self.hoods.get_all()

    def __del__(self):

        # close driver
        self.driver.quit()

    def __repr__(self):

        string = "Data Gathered({}):\n".format(self.last_update)

        string += json.dumps(self.data, sort_keys=True, indent=4)

        return string

# testting
if( __name__ == "__main__" ):
    scavanger = CovidScraper(headless=False)
    scavanger.get_all()
    print(scavanger)