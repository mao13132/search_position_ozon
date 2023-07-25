import time

from src.google.google_write_data import GoogleWriteData
from src.ozon.job_article import JobArticle
from src.ozon.start_ozon import StartOzon


class StartIter:
    def __init__(self, driver, dict_job, google_core):
        self.driver = driver
        self.dict_job = dict_job
        self.google_core = google_core

    def start_iter(self):

        ozon_core = StartOzon(self.driver)

        res_load_ozon = ozon_core.start_load_ozon()

        # TODO авторизация

        if not res_load_ozon:
            return False

        res_click = ozon_core.click_get_search()

        change_core = GoogleWriteData(self.google_core)

        # TODO кликнуть на поиск позиций

        for job in self.dict_job:

            if job['request'] == '':
                continue

            input_data_list = ozon_core.get_input_list()

            if not input_data_list:
                print(f'Не могу определить поля для заполнения в ozon')
                continue

            res_job_article = JobArticle(self.driver, ozon_core).start_job_article(job['article'], input_data_list[2])

            if not res_job_article:
                continue

            print()
