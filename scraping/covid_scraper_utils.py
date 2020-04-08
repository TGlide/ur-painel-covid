from selenium.webdriver.common.by import By # type of query for locating elements
from selenium.webdriver.support.ui import WebDriverWait # wait until condition is fullfiled
from selenium.webdriver.support import expected_conditions as EC # condition to be fullfiled
from selenium.webdriver.common.action_chains import ActionChains # perform user interaction actions
from selenium.webdriver.common.keys import Keys # common keys

from time import sleep

def dropdown_menu_set(driver, navbar, option, timeout=0):

    # find dropdown menu
    dropdown_menu = navbar.find_element(By.XPATH, "div[3]/div[2]/div/div/div[2]/div/a")

    # click it!
    dropdown_menu.click()
    
    # let's perform some interaction actions 
    actions = ActionChains(driver)

    actions.send_keys(option)

    # press ENTER to select the desired option
    actions.send_keys(Keys.ENTER).perform()

    # wait for results to take effect
    sleep(timeout)

def change_to_right_subpanel(dashboard, subpanel_num):

    # get path to the right subpanel
    path_to_subpanel = "div[26]/margin-container/full-container/div/nav/span[{}]".format(subpanel_num)

    WebDriverWait(dashboard, 10).until(
        EC.element_to_be_clickable((By.XPATH, path_to_subpanel))
    ).click()

def change_to_bottom_subpanel(dashboard, subpanel_num):

    # get path to the right subpanel
    path_to_subpanel = "div[25]/margin-container/full-container/div/nav/span[{}]".format(subpanel_num)

    # find it and click it
    WebDriverWait(dashboard, 10).until(
        EC.element_to_be_clickable((By.XPATH, path_to_subpanel))
    ).click()