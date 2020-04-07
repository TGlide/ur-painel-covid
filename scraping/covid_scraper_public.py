class CovidScraperPublic():

    def __init__(self, dashboard):

        self.data = {
            'hospitalized': None,
            'interned': None,
            'dead': None
        }

        self.dashboard = dashboard