import time
from datetime import datetime

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckCity:
    def __init__(self, driver):
        self.driver = driver
        self.links_post = []
        self.source_name = 'Ozon'

    def get_city(self):
        try:
            city = self.driver.find_element(by=By.XPATH, value=f"//*[contains(@data-widget, 'addressBookBarWeb')]").text
        except:
            return ''

        return city

    def click_change_city(self):
        try:
            self.driver.find_element(by=By.XPATH, value=f"//*[contains(text(), "
                                                        f"'Укажите адрес доставки')]//parent::span"
                                                        f"//parent::button").click()
        except:
            return False

        return True

    def click_change_popup(self):
        try:
            self.driver.find_element(by=By.XPATH, value=f"//*[contains(@data-widget, 'commonAddressBook')]"
                                                        f"//*[contains(text(), 'Изменить')]").click()
        except:
            return False

        return True

    def click_moscow(self):
        try:
            self.driver.find_elements(by=By.XPATH, value=f"//*[contains(@data-widget, 'citySelector')]"
                                                         f"//*[contains(text(), 'Москва')]//parent::div")[0].click()
        except:
            return False

        return True

    def check_load_popup(self):
        try:
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(@data-widget, 'commonAddressBook')]"
                                                          f"//*[contains(text(), 'Выбрать на карте')]")))
            return True
        except:
            return False

    def check_city_selector_popup(self):
        try:
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(@data-widget, 'citySelector')]"
                                                          f"//*[contains(text(), 'Москва')]")))
            return True
        except:
            return False

    def loop_change_city(self):

        count = 0
        count_try = 5

        while True:
            count += 1
            if count > count_try:
                print(f'Не смог открыть popup смены города')
                return False

            res_click = self.click_change_city()

            if not res_click:
                continue

            res_open_popup = self.check_load_popup()

            if not res_open_popup:
                continue

            res_change_popup = self.click_change_popup()

            if not res_change_popup:
                continue

            res_open_inser_city_popup = self.check_city_selector_popup()

            if not res_open_inser_city_popup:
                continue

            res_insert_moscow = self.click_moscow()

            if not res_insert_moscow:
                continue

            return True


    def loop_insert_city(self):
        count = 0
        count_try = 5
        while True:
            count += 1
            if count > count_try:
                print(f'Не смог сменить город на Москву')
                return False

            city = self.get_city()

            if 'Москва' in city:
                return True

            res_change_city = self.loop_change_city()

            if res_change_city:
                return True

            time.sleep(1)

    def start_check(self):
        insert_moscov = self.loop_insert_city()

        print()

        return insert_moscov
