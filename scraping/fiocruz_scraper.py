from kaggle.api.kaggle_api_extended import KaggleApi # to get states csv
from urllib.request import urlretrieve # get csv file from brasil.io (cities)
import os # set environmental variables to use kaggle

class FiocruzScraper():

    def __init__(self, folder):

        self.states_url = "unanimad/corona-virus-brazil"
        self.cities_url = "https://brasil.io/dataset/covid19/caso?format=csv"

        self.folder = folder if folder[-1] == '/' else folder + '/'

        self.kapi = KaggleApi()

        self.kapi.authenticate()

    def download_states(self):

        filename = 'brazil_covid19.csv'

        self.kapi.dataset_download_file(self.states_url, filename, self.folder)

        # reaname file, since Kaggle won't do it for us
        os.rename(self.folder + filename, self.folder + "states.csv")

    def download_cities(self):

        urlretrieve(self.cities_url, self.folder + "cities.csv")

    def download(self):
        self.download_states()
        self.download_cities()

if( __name__ == "__main__" ):

    scraper = FiocruzScraper(folder="data")
    scraper.download()