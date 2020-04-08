from selenium import webdriver # webdriver for automated browser
from selenium.webdriver.firefox.options import Options # options for the browser
from selenium.webdriver.common.by import By # type of query for locating elements
from selenium.webdriver.support.ui import WebDriverWait # wait until condition is fullfiled
from selenium.webdriver.support import expected_conditions as EC # condition to be fullfiled

import os
'''
NOTE: this code is NOT, in under NO circunstance, UTTER GARBAGE
I WILL NOT, i repeat, I WILL NOT ALLOW SUCH THING TO BE SAID TO GARBAGE
seriously don't use it, i just did as a little thing to know when the page
is not under maintence anymore (and yes it didn't work at first)
'''
def setup_driver(timeout=300):

    # set starting URL and if we will run headless or not
    options = Options()
    options.headless = True
    options.add_argument("https://experience.arcgis.com/experience/38efc69787a346959c931568bd9e2cc4")

    # initialize browser
    driver = webdriver.Firefox(options = options)

    # tell the driver to wait if element being searched isn't found at first (default: 5 min)
    driver.implicitly_wait(timeout)

    # get iframe with all the data and switch to it
    iframe = WebDriverWait(driver, timeout).until(
        EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe")) # get iframe
    )

    return driver

def check_if_available():
    driver = setup_driver()
    
    ok=False
    while(not ok):

        navbar = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[@class='margin-container']/div[@class='full-container']/div")
    
        # get text in navbar containing the time it was last updated
        last_update_str = navbar.find_element(By.XPATH, "div[2]/div[2]").text

        # check if page is under maintance right now
        if( last_update_str == None or "atualização" in last_update_str):

            print("peeeeeeeera")
            driver.refresh()
        else:
            ok=True
            driver.quit()
            print("TUXI CATUM TICA TUM")
            os.system("mpg123 alarm")

        print(last_update_str)

if( __name__ == "__main__" ):
    while(1):
        try:
            check_if_available()
        except KeyboardInterrupt:
            break
        except:
            pass