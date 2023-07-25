import time

from src.google.google_write_data import GoogleWriteData
from src.ozon.start_ozon import StartOzon


class StartIter:
    def __init__(self, driver, dict_job, google_core):
        self.driver = driver
        self.dict_job = dict_job
        self.google_core = google_core

    def start_iter(self):

        ozon_core = StartOzon(self.driver)

        change_core = GoogleWriteData(self.google_core)

        for job in self.dict_job:

            if 'ozon' not in job['link']:
                continue

            price = ozon_core.start_pars(job['link'])

            if not price:
                continue

            job['price'] = price

            print(f'Получил цену: "{price}"')

            change_core.write_data(job)

            time.sleep(30)



