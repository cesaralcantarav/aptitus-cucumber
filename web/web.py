
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Web(object):
    __TIMEOUT = 10
    def __init__(self, web_driver):
        super(Web, self).__init__()  # in python 3.6 you can just call super().__init__()
        self._web_driver_wait = WebDriverWait(web_driver, Web.__TIMEOUT)
        self._web_driver = web_driver

    def open(self, url):
        self._web_driver.get(url)


    def find_by_id(self, selector):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.ID, selector)))

    def find_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    
    def finds_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    # select  by name
    def find_by_name(self, name):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))
    
    def find_by_class_name(self, class_name):
       return self._web_driver_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))

    def time_sleep(self):
        return time.sleep(5)