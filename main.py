import os

# from src.browser.createbrowser import CreatBrowser
from src.browser.createbrowser_uc import CreatBrowser

from src.google.google_modul import GoogleModul

from src.google.google_start import GoogleStart

from src.start_iter import StartIter


def main():

    google_core = GoogleModul(os.getcwd()).connect_sheet()

    # data_pars_dict = GoogleStart(google_core).start_get_data()

    data_pars_dict = [{'competitor': 'Запрос 1', 'request': 'чайник заварочный', 'name_sheet': 'Benerich', 'x': 4, 'y': 'E2', 'price_index': 'F2', 'article': 'BNR00022'}, {'competitor': 'Запрос 1', 'request': 'чайник заварочный', 'name_sheet': 'Benerich', 'x': 4, 'y': 'E3', 'price_index': 'F3', 'article': 'BNR00033'}, {'competitor': 'Запрос 1', 'request': 'банки для сыпучих продуктов', 'name_sheet': 'Benerich', 'x': 4, 'y': 'E4', 'price_index': 'F4', 'article': 'BNR00034'}]

    print(f'\nПолучил товары для парсинга')

    browser = CreatBrowser()

    res_job = StartIter(browser.driver, data_pars_dict, google_core).start_iter()

    print(f'\nРабота завершена')


if __name__ == '__main__':
    main()
