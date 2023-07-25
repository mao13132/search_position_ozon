from settings import ID_SHEET


class GoogleGetNameColums:
    def __init__(self, google_core):
        self.google_core = google_core
        self.service = google_core.service

    def get_name_columns(self, name_sheet):

        try:

            self.values = self.service.spreadsheets().values().get(
                spreadsheetId=ID_SHEET,
                range=f'{name_sheet}!A1:BB1',
                majorDimension='ROWS'
            ).execute()

        except Exception as es:
            print(f'🚫 Ошибка при подключении к Google ({name_sheet}) таблицам "{es}"')

            return False

        return self.values

    @staticmethod
    def get_index_competitor(list_name_columns):
        ip_list_index = []
        for count, colm in enumerate(list_name_columns['values'][0]):

            _temp_ip = {}

            if 'Конкурент' in colm:
                _temp_ip['name'] = colm
                _temp_ip['index'] = count

                ip_list_index.append(_temp_ip)

        return ip_list_index
