import os
import time

from settings import GET_INDEX_SAVE_PRODUCTS, JOB_POSITION_SEO
from src.browser.createbrowser_uc import CreatBrowser

from src.google.google_modul import GoogleModul

from src.google.google_start import GoogleStart
from src.google.time_ower_save import TimeOwerSave
from src.ozon.job_geography import JobGeography

from src.start_iter import StartIter
from src.telegram_debug import SendlerOneCreate


def main():
    google_core = GoogleModul(os.getcwd()).connect_sheet()

    browser = CreatBrowser()

    if GET_INDEX_SAVE_PRODUCTS:

        print(f'\nНачинаю сбор индекса локализации и дней хранения\n')

        job_geogr = JobGeography(browser.driver, google_core).start_geography()

        time.sleep(5)

        TimeOwerSave(google_core).write_time('Сбор индекса-хранения')

    if JOB_POSITION_SEO:

        data_pars_dict = GoogleStart(google_core).start_get_data()

        print(f'\nПолучил поисковые запроса для проверки их позиций\n')

        res_job = StartIter(browser.driver, data_pars_dict, google_core).start_iter()

        TimeOwerSave(google_core).write_time('Сбор позиций')

    print(f'\nРабота завершена')


if __name__ == '__main__':
    try:
        main()
    except Exception as es:
        SendlerOneCreate('').save_text(f'Ozon поиск позиций упал *.246 "{es}"')
