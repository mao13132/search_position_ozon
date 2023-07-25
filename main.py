import os

from src.browser.createbrowser_uc import CreatBrowser

from src.google.google_modul import GoogleModul

from src.google.google_start import GoogleStart

from src.start_iter import StartIter


def main():
    google_core = GoogleModul(os.getcwd()).connect_sheet()

    data_pars_dict = GoogleStart(google_core).start_get_data()

    print(f'\nПолучил товары для парсинга')

    browser = CreatBrowser()

    res_job = StartIter(browser.driver, data_pars_dict, google_core).start_iter()

    print(f'\nРабота завершена')


if __name__ == '__main__':
    main()
