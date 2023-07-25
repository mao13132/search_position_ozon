from settings import ID_SHEET
from src.google._slovar import colums_slovar


class GoogleGetData:
    def __init__(self, google_core, name_index_list, article_list):
        self.google_core = google_core
        self.service = google_core.service
        self.name_index_list = name_index_list
        self.count_load_rows = 100000
        self.article_list = article_list

    def get_columns(self, x, y, name_sheet):
        self.values = self.service.spreadsheets().values().get(
            spreadsheetId=ID_SHEET,
            range=f'{name_sheet}!{x}:{y}',
            majorDimension='ROWS'
        ).execute()
        try:
            self.values = self.values['values']
        except Exception as es:
            return []

        return self.values

    def insert_x_y_dict(self, competitor, result_dict, name_sheet):

        good_dict = []

        y_start = 2

        for count, row in enumerate(result_dict):

            product = {}

            product['competitor'] = competitor['name']

            try:
                product['link'] = row[0]
            except:
                product['link'] = ''

            product['name_sheet'] = name_sheet
            product['x'] = competitor['index']
            product['y'] = f"{colums_slovar[competitor['index']]}{y_start + count}"
            product['price_index'] = f"{colums_slovar[competitor['index'] + 1]}{y_start + count}"
            product['article'] = self.article_list[count][0]

            good_dict.append(product)

        return good_dict

    def start_get_data(self, name_sheet):

        good_dict_data = []

        for competitor in self.name_index_list:

            x = f"{colums_slovar[competitor['index']]}2"

            y = f"{colums_slovar[competitor['index']]}{self.count_load_rows}"

            _row_table = self.get_columns(x, y, name_sheet)

            if _row_table == []:
                print(f'На вкладке {name_sheet} у {competitor["name"]} не обнаружено данных')
                continue

            _good_dict_data = self.insert_x_y_dict(competitor, _row_table, name_sheet)

            good_dict_data.extend(_good_dict_data)

        return good_dict_data
