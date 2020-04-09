from selenium.webdriver.common.by import By # type of query for locating elements

from covid_scraper_utils import change_to_bottom_subpanel

class CovidScraperGraph():

    def __init__(self, dashboard):

        self.data = {
            'dead': None,
            'confirmed': None,
            'hospitalized': None,
            'interned': None
        }

        # first subpanel
        self.confirmed_graph_path = "/html/body/div/div/div[2]/div/div/div/margin-container/full-container/div[22]/margin-container/full-container/div/div[2]/div/div/div[1]/*[name()='svg']/*[name()='g'][12]/*[name()='g'][2]"
        self.dead_graph_path = "/html/body/div/div/div[2]/div/div/div/margin-container/full-container/div[22]/margin-container/full-container/div/div[2]/div/div/div[1]/*[name()='svg']/*[name()='g'][12]/*[name()='g'][1]"

        # first subpanel
        self.hospitalized_graph_path = "/html/body/div/div/div[2]/div/div/div/margin-container/full-container/div[25]/margin-container/full-container/div/div[2]/div/div/div[1]/*[name()='svg']/*[name()='g'][12]/*[name()='g'][1]"
        self.interned_graph_path = "/html/body/div/div/div[2]/div/div/div/margin-container/full-container/div[25]/margin-container/full-container/div/div[2]/div/div/div[1]/*[name()='svg']/*[name()='g'][12]/*[name()='g'][2]"

        self.dashboard = dashboard

    def get_dead(self):

        change_to_bottom_subpanel(self.dashboard, 1)

        # numbers will come separated by space, parse them and then convert each one to int
        dead_graph = self.dashboard.find_element(By.XPATH, self.dead_graph_path)

        # iterate through tspan tags inside graph (where the numbers are)
        contents = [ tspan.text.replace(",", "") for tspan in dead_graph.find_elements(By.XPATH, "*[name()='text']/*[name()='tspan']")]

        self.data['dead'] = list(map(int, contents))

        return self.data['dead']

    def get_confirmed(self):

        change_to_bottom_subpanel(self.dashboard, 1)

        # numbers will come separated by space, parse them and then convert each one to int
        confirmed_graph = self.dashboard.find_element(By.XPATH, self.confirmed_graph_path)
        
        # iterate through tspan tags inside graph (where the numbers are)
        contents = [ tspan.text.replace(",", "") for tspan in confirmed_graph.find_elements(By.XPATH, "*[name()='text']/*[name()='tspan']")]

        self.data['confirmed'] = list(map(int, contents))

        return self.data['confirmed']

    def get_hospitalized(self):

        change_to_bottom_subpanel(self.dashboard, 4)

        # numbers will come separated by space, parse them and then convert each one to int
        hospitalized_graph = self.dashboard.find_element(By.XPATH, self.hospitalized_graph_path)

        # iterate through tspan tags inside graph (where the numbers are)
        contents = [ tspan.text.replace(",", "") for tspan in hospitalized_graph.find_elements(By.XPATH, "*[name()='text']/*[name()='tspan']")]
        print(contents)
        self.data['hospitalized'] = list(map(int, contents))

        return self.data['hospitalized']

    def get_interned(self):

        change_to_bottom_subpanel(self.dashboard, 4)

        # numbers will come separated by space, parse them and then convert each one to int
        interned_graph = self.dashboard.find_element(By.XPATH, self.interned_graph_path)

        # iterate through tspan tags inside graph (where the numbers are)
        contents = [ tspan.text.replace(",", "") for tspan in interned_graph.find_elements(By.XPATH, "*[name()='text']/*[name()='tspan']")]

        self.data['interned'] = list(map(int, contents))

        return self.data['interned']

    def get_all(self):

        self.get_dead()
        self.get_confirmed()
        self.get_hospitalized()
        self.get_interned()

        return self.data