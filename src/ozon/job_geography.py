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

    def job_one_cabinet(self, name_cabinet_name, ozon_core):

        cabinet_core = JobCabinet(self.driver)

        change_core = GoogleWriteData(self.google_core)

        for count, cabinet in enumerate(name_cabinet_name):

            valid_cabinet_name = cabinet_core.check_name_cabinet(cabinet)

            if not valid_cabinet_name:
                print(f'Переключаю кабинет на {cabinet}')
                res_change_cabinet = cabinet_core.start_job_cabinet(cabinet)

            res_load_ozon = ozon_core.load_ozon_geograph()

            procent = self.get_procent_local()

            y = count + 2

            change_core.write_procent_geograph(procent, y)

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

        print()
