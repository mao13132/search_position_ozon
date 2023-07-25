from settings import NAME_SHEET
from src.google._google_get_sheets_name import GoogleGetSheetsName
from src.google.google_get_name_colums import GoogleGetNameColums
from src.google.google_get_data import GoogleGetData


class GoogleStart:
    def __init__(self, google_core):
        self.google_core = google_core

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
                print(f'На вкладке {name_sheet} не обнаружены столбцы с конкурентами')
                continue

            dict_job_one_sheet = GoogleGetData(self.google_core, name_index_list).start_get_data(name_sheet)

            good_all_job.extend(dict_job_one_sheet)

        return good_all_job
