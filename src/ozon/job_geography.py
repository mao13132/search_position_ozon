import time

from src.google._slovar import colums_slovar
from src.google.google_get_name_colums import GoogleGetNameColums
from src.google.google_write_data import GoogleWriteData
from src.ozon.job_cabinet import JobCabinet
from src.ozon.start_ozon import StartOzon

from selenium.webdriver.common.by import By


class JobGeography:
    def __init__(self, driver, google_core):
        self.driver = driver
        self.google_core = google_core

    def get_procent_local(self):
        try:
            procent = self.driver.find_element(by=By.XPATH,
                                               value=f"//article[contains(@class, 'totalLocalizationWidget')]"
                                                     f"//*[contains(@class, 'totalValue')]").text
        except:
            return ''

        return procent

    def _formated_value(self, value: str):
        _value = ''
        for x in value:
            if x.isdigit():
                _value += x

        try:
            _value = int(_value)
        except:
            return 0

        return _value

    def get_cost_day(self):
        try:
            day_cost = self.driver.find_element(by=By.XPATH,
                                                value=f"//*[contains(text(), 'дней')]").text
        except:
            return ''

        day_cost = self._formated_value(day_cost)

        return day_cost

    def loop_get_cost(self):
        count = 0
        count_try = 5
        while True:
            count += 1
            if count > count_try:
                return 0

            day_cost = self.get_cost_day()

            if day_cost != '':
                return day_cost

            if count > 1:
                time.sleep(1)




    def job_one_cabinet(self, name_cabinet_name, ozon_core):

        cabinet_core = JobCabinet(self.driver)

        change_core = GoogleWriteData(self.google_core)

        for count, cabinet in enumerate(name_cabinet_name):

            valid_cabinet_name = cabinet_core.check_name_cabinet(cabinet)

            if not valid_cabinet_name:
                print(f'Переключаю кабинет на {cabinet}')
                res_change_cabinet = cabinet_core.start_job_cabinet(cabinet)

                if not res_change_cabinet:
                    print(f'Не смог переключить кабинет')
                    y = count + 2
                    change_core.write_procent_geograph('Нет доступа', 'Нет доступа', y)
                    continue

            res_load_ozon = ozon_core.load_ozon_geograph()

            procent = self.get_procent_local()

            res_load_ozon = ozon_core.load_ozon_cost()

            cost = self.loop_get_cost()

            y = count + 2

            change_core.write_procent_geograph(procent, cost, y)

            print(f'Вписал процент географии в {cabinet}')

        return True

    def start_geography(self):
        ozon_core = StartOzon(self.driver)

        res_load_ozon = ozon_core.start_load_ozon()

        if not res_load_ozon:
            return False

        name_columns = GoogleGetNameColums(self.google_core).get_geography_cabinet_name()

        if not name_columns:
            return False

        name_cabinet_name = [x for x in name_columns['values'][0]]

        res_job_cabinet = self.job_one_cabinet(name_cabinet_name, ozon_core)

        print(f'Закончил ')
