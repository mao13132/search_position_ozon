import time

from src.google.google_write_data import GoogleWriteData
from src.ozon.job_article import JobArticle
from src.ozon.job_get_result import GetGetResult
from src.ozon.job_region import JobRegion
from src.ozon.job_request_search import JobRequestsSearch
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

            res_job_region = JobRegion(self.driver).start_job_region(input_data_list[1], 'Москва')

            res_insert_requests = JobRequestsSearch(self.driver).start_job_search(input_data_list[0], job['request'])

            res_finish_click_but = ozon_core.finish_button_search()

            res_good_res = ozon_core.check_load_good(f"//tbody//tr[contains(@class, 'row')]//td")

            result = GetGetResult(self.driver).start_job_get_result()

            job['position'] = result

            change_core.write_data(job)

            print()

        return True
