from selenium.webdriver.common.by import By # type of query for locating elements

class CovidScraperHood():

    def __init__(self, dashboard):

        # where all the gathered data will be kept
        self.data = {
        }

        self.dashboard = dashboard

    def get_neighborhood(self, hood_element):

        # to make sure we can parse the number properly
        preprocessing = lambda str: str.replace(",", "").replace(".", "") 

        # get contents out of the tag and feed it to self.data
        contents = hood_element.find_element(By.XPATH, "div/div/p")

        key = contents.find_element(By.XPATH, "span[2]").text

        value = preprocessing(contents.find_element(By.XPATH, "span[1]").text)

        self.data[key] = value

        return self.data[key]

    def get_neighborhoods(self):

        # iterate over the neighborhood tags and gather data from each one
        hood_list = "div[3]/margin-container/full-container/div/div[2]/nav/span"
        for neighborhood in self.dashboard.find_elements(By.XPATH, hood_list):

            self.get_neighborhood(neighborhood)

        return self.data

    def get_all(self):

        return self.get_neighborhoods()