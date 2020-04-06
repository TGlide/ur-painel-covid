from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class DataScraper:

    def __init__(self, binary_path="geckodriver"):

        # set starting URL
        options = Options()
        options.add_argument("https://experience.arcgis.com/experience/38efc69787a346959c931568bd9e2cc4")

        # initialize browser
        self.driver = webdriver.Firefox(options = options, executable_path=binary_path)

    def __del__(self):

        # close driver
        self.driver.close()

# testting
if( __name__ == "__main__" ):
    driver = DataScraper()