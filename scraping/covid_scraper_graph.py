from selenium.webdriver.common.by import By # type of query for locating elements

from time import sleep

class CovidScraperGraph():

    def __init__(self, dashboard):

        self.data = {
            'dead': None,
            'confirmed': None
        }

        self.confirmed_graph_path = "/html/body/div/div/div[2]/div/div/div/margin-container/full-container/div[19]/margin-container/full-container/div/div[2]/div/div/div[1]/*[name()='svg']/*[name()='g'][12]/*[name()='g'][2]"
        self.dead_graph_path = "/html/body/div/div/div[2]/div/div/div/margin-container/full-container/div[19]/margin-container/full-container/div/div[2]/div/div/div[1]/*[name()='svg']/*[name()='g'][12]/*[name()='g'][1]"

        self.dashboard = dashboard

    def get_dead(self):

        # numbers will come separated by space, parse them and then convert each one to int
        dead_graph = self.dashboard.find_element(By.XPATH, self.dead_graph_path)

        # iterate through tspan tags inside graph (where the numbers are)
        contents = [ tspan.text.replace(",", "") for tspan in dead_graph.find_elements(By.XPATH, "*[name()='text']/*[name()='tspan']")]

        self.data['dead'] = list(map(int, contents))

        return self.data['dead']

    def get_confirmed(self):

        # numbers will come separated by space, parse them and then convert each one to int
        confirmed_graph = self.dashboard.find_element(By.XPATH, self.confirmed_graph_path)
        
        # iterate through tspan tags inside graph (where the numbers are)
        contents = [ tspan.text.replace(",", "") for tspan in confirmed_graph.find_elements(By.XPATH, "*[name()='text']/*[name()='tspan']")]

        self.data['confirmed'] = list(map(int, contents))

        return self.data['confirmed']

    def get_all(self):

        self.get_dead()
        self.get_confirmed()

        return self.data