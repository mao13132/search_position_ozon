import time

from settings import NAME_SHEET, ID_SHEET
from src.google._google_get_sheets_name import GoogleGetSheetsName
from src.google._slovar import colums_slovar
from src.google.google_get_name_colums import GoogleGetNameColums
from src.google.google_get_data import GoogleGetData


class GoogleStart:
    def __init__(self, google_core):
        self.google_core = google_core
        self.count_load_rows = 100000

    def _get_article(self, x, y, name_sheet):
        values = self.google_core.service.spreadsheets().values().get(
            spreadsheetId=ID_SHEET,
            range=f'{name_sheet}!{x}:{y}',
            majorDimension='ROWS'
        ).execute()
        try:
            values = values['values']
        except:
            return []

        return values

    def get_article(self, article, name_sheet):

        x = f"{colums_slovar[article]}2"

        y = f"{colums_slovar[article]}{self.count_load_rows}"

        article_list = self._get_article(x, y, name_sheet)

        return article_list

    def start_get_data(self):

        if NAME_SHEET == []:
            names_list_sheet = GoogleGetSheetsName(self.google_core).get_name_sheets()
        else:
            names_list_sheet = NAME_SHEET

        good_all_job = []

        #   Итерация страниц по их именам
        for name_sheet in names_list_sheet:

            print(f'Получаю данные с вкладки {name_sheet}')

            name_columns = GoogleGetNameColums(self.google_core).get_name_columns(name_sheet)

            if not name_columns:
                continue

            name_index_list = GoogleGetNameColums.get_index_competitor(name_columns)

            if name_index_list == []:
                print(f'На вкладке {name_sheet} не обнаружены столбцы с запросами')
                continue

            article = name_index_list[0]['article_inx']

            article_list = self.get_article(article, name_sheet)

            dict_job_one_sheet = GoogleGetData(self.google_core, name_index_list, article_list).start_get_data(
                name_sheet)

            good_all_job.extend(dict_job_one_sheet)

            time.sleep(5)

        return good_all_job
