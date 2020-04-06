from selenium import webdriver # webdriver for automated browser
from selenium.webdriver.firefox.options import Options # options for the browser
from selenium.webdriver.common.by import By # type of query for locating elements
from selenium.webdriver.support.ui import WebDriverWait # wait for condition to be fullfiled when looking for element
from selenium.webdriver.support import expected_conditions as EC # condition to be fullfiled

from datetime import datetime

class CovidScraper:

    def __init__(self, headless=True, timeout=300, binary_path="geckodriver"):

        # where all the gathered data will be kept
        self.data = {
            'confirmed': None,
            'possible': None,
            'recovered': None
        }

        # initialize the driver at the dashboard URL
        self.driver = self.setup_driver(headless, timeout, binary_path)

        # get time of the last update (if it is in maintenance, None will be returned)
        self.last_update = self.page_status()

        # get main dashboard tag (so we don't need to search from root everytime)
        if( self.last_update ): self.dashboard = self.driver.find_element(By.XPATH, "//html/body/div/div/div[2]/div/div/div/margin-container/full-container")

    def setup_driver(self, headless, timeout, binary_path):

        # set starting URL and if we will run headless or not
        options = Options()
        options.headless = headless
        options.add_argument("https://experience.arcgis.com/experience/38efc69787a346959c931568bd9e2cc4")

        # initialize browser
        driver = webdriver.Firefox(options = options, executable_path=binary_path)

        # tell the driver to wait if element being searched isn't found at first (default: 5 min)
        driver.implicitly_wait(timeout)

        # get iframe with all the data and switch to it
        iframe = driver.find_element(By.XPATH, "//iframe") # get iframe
        driver.switch_to.frame(iframe)

        return driver

    def page_status(self):

        # get navbar
        navbar = self.driver.find_element(By.XPATH, "//body/div/div/div[1]/div[@class='margin-container']/div[@class='full-container']/div")

        # get text in navbar containing the time it was last updated
        last_update_str = navbar.find_element(By.XPATH, "div[2]/div[2]").text

        # check if page is under maintance right now
        if( last_update_str == None or "atualização" in  last_update_str):
            last_update = None   
        else:
            # if not, get the time of the last update
            last_update = datetime.strptime(last_update_str, "boletim de %d/%m/%Y %H:%M - SMS | IPP | COR")

        return last_update

    def __del__(self):

        # close driver
        self.driver.quit()

    def __repr__(self):

        string = "Data Gathered({}):\n".format(self.last_update)

        for key in self.data:
            string + "{} : {}\n".format(key, self.data[key])

        return string

    '''
        all the methods from this point on have the purpose
        of getting the data and feeding it to the 'data' attribute
    '''
    def get_confirmed_cases(self):

        # get number of confirmed cases and convert it to a numeric type
        self.data['confirmed'] = int(self.dashboard.find_element(
            By.XPATH,
             "//div[1]/margin-container/full-container/div/div/div/div[2]/svg/g[2]/svg/text"
             ).text.replace(",", "."))

# testting
if( __name__ == "__main__" ):
    scavanger = CovidScraper(headless=False)
    scavanger.get_confirmed_cases()
    print(scavanger)