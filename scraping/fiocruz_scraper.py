from urllib.request import urlretrieve

class FiocruzScraper():

    def __init__(self, folder):

        self.states_url = "https://www.kaggle.com/unanimad/corona-virus-brazil/download"
        self.cities_url = "https://brasil.io/dataset/covid19/caso?format=csv"

        self.folder = folder if folder[-1] == '/' else folder + '/'

    def download_states(self):

        urlretrieve(self.states_url, self.folder + "states.csv")

    def download_cities(self):

        urlretrieve(self.cities_url, self.folder + "cities.csv")

    def download(self):
        self.download_states()
        self.download_cities()

if( __name__ == "__main__" ):

    scraper = FiocruzScraper(folder="data")
    scraper.download()