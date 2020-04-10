from selenium.webdriver.common.by import By # type of query for locating elements

from covid_scraper_utils import change_to_bottom_subpanel

from datetime import datetime, timedelta
import csv

class CovidScraperGraph():

    def __init__(self, dashboard, last_date):

        self.data = {
            'dead': None,
            'confirmed': None,
            'hospitalized': None,
            'uti': None
        }

        # first subpanel
        self.confirmed_graph_path = "/html/body/div/div/div[2]/div/div/div/margin-container/full-container/div[22]/margin-container/full-container/div/div[2]/div/div/div[1]/*[name()='svg']/*[name()='g'][12]/*[name()='g'][2]"
        self.dead_graph_path = "/html/body/div/div/div[2]/div/div/div/margin-container/full-container/div[22]/margin-container/full-container/div/div[2]/div/div/div[1]/*[name()='svg']/*[name()='g'][12]/*[name()='g'][1]"

        # first subpanel
        self.hospitalized_graph_path = "/html/body/div/div/div[2]/div/div/div/margin-container/full-container/div[25]/margin-container/full-container/div/div[2]/div/div/div[1]/*[name()='svg']/*[name()='g'][12]/*[name()='g'][1]"
        self.uti_graph_path = "/html/body/div/div/div[2]/div/div/div/margin-container/full-container/div[25]/margin-container/full-container/div/div[2]/div/div/div[1]/*[name()='svg']/*[name()='g'][12]/*[name()='g'][2]"

        self.dashboard = dashboard
        self.last_date = last_date

    def get_dead(self):

        change_to_bottom_subpanel(self.dashboard, 1)

        # numbers will come separated by space, parse them and then convert each one to int
        dead_graph = self.dashboard.find_element(By.XPATH, self.dead_graph_path)

        # iterate through tspan tags inside graph (where the numbers are)
        contents = [ tspan.text.replace(",", "") for tspan in dead_graph.find_elements(By.XPATH, "*[name()='text']/*[name()='tspan']")]

        self.data['dead'] = self.add_dates(list(map(int, contents)))

        return self.data['dead']

    def get_confirmed(self):

        change_to_bottom_subpanel(self.dashboard, 1)

        # numbers will come separated by space, parse them and then convert each one to int
        confirmed_graph = self.dashboard.find_element(By.XPATH, self.confirmed_graph_path)
        
        # iterate through tspan tags inside graph (where the numbers are)
        contents = [ tspan.text.replace(",", "") for tspan in confirmed_graph.find_elements(By.XPATH, "*[name()='text']/*[name()='tspan']")]

        self.data['confirmed'] = self.add_dates(list(map(int, contents)))

        return self.data['confirmed']

    def get_hospitalized(self):

        change_to_bottom_subpanel(self.dashboard, 4)

        # numbers will come separated by space, parse them and then convert each one to int
        hospitalized_graph = self.dashboard.find_element(By.XPATH, self.hospitalized_graph_path)

        # iterate through tspan tags inside graph (where the numbers are)
        contents = [ tspan.text.replace(",", "") for tspan in hospitalized_graph.find_elements(By.XPATH, "*[name()='text']/*[name()='tspan']")]

        self.data['hospitalized'] = self.add_dates(list(map(int, contents)))

        return self.data['hospitalized']

    def get_uti(self):

        change_to_bottom_subpanel(self.dashboard, 4)

        # numbers will come separated by space, parse them and then convert each one to int
        uti_graph = self.dashboard.find_element(By.XPATH, self.uti_graph_path)

        # iterate through tspan tags inside graph (where the numbers are)
        contents = [ tspan.text.replace(",", "") for tspan in uti_graph.find_elements(By.XPATH, "*[name()='text']/*[name()='tspan']")]

        self.data['uti'] = self.add_dates(list(map(int, contents)))

        return self.data['uti']

    def get_value_from_sequence(self, sequence_name, date):

        for d in self.data[sequence_name].keys():
            if( d == date ):
                return self.data[sequence_name][d]

        return 0

    def add_dates(self, numbers):

        n_days = len(numbers)

        # turn every value in a list to a dictionary with the date as key to the value
        return { self.last_date - timedelta(days=n_days-1-i) : value for i, value in enumerate(numbers) }

    def to_csv(self, filename):

        # get biggest list
        n_rows = max(list(map(len, [ self.data[key] for key in self.data ])))

        with open(filename, "w") as f:
            fieldnames = ['date', 'confirmed', 'dead', 'hospitalized', 'uti']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            # write header
            writer.writeheader()

            # start writing from the oldest date
            for date in [ self.last_date -  timedelta(days=i) for i in range(n_rows)]:

                # write row
                writer.writerow({
                    'date': str(date.date()),
                    'confirmed': self.get_value_from_sequence('confirmed', date),
                    'dead': self.get_value_from_sequence('dead', date),
                    'hospitalized': self.get_value_from_sequence('hospitalized', date),
                    'uti': self.get_value_from_sequence('uti', date),
                })

    def get_all(self):

        self.get_dead()
        self.get_confirmed()
        self.get_hospitalized()
        self.get_uti()

        return self.data