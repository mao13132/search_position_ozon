import time
from datetime import datetime

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.ozon.check_city import CheckCity
from src.ozon.load_page import LoadPage


class StartOzon():
    def __init__(self, driver):
        self.driver = driver
        self.links_post = []
        self.source_name = 'Ozon'

    def formated_price(self, value):
        _price = ''

        try:

            for x in value:
                if x.isdigit():
                    _price += x

            _price = int(_price)
        except:
            _price = value


        return _price

    def get_price(self):
        try:
            price = self.driver.find_element(by=By.XPATH, value=f"//*[contains(@data-widget, 'webPrice')]//button").text
        except:
            price = 0

        price = self.formated_price(price)

        return price

    def start_pars(self, link):

        result_start_page = LoadPage(self.driver, link).loop_load_page(f"//*[contains(@data-widget, 'webPrice')]")

        if not result_start_page:
            return False

        change_city_to_moscow = CheckCity(self.driver).start_check()

        price = self.get_price()

        return price
