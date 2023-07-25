from settings import ID_SHEET, BLACK_NAME


class GoogleGetSheetsName:
    def __init__(self, google_core):
        self.google_core = google_core
        self.service = google_core.service

    def get_name_sheets(self):

        # Пример чтения файла
        try:
            self.connect = self.service.spreadsheets().get(spreadsheetId=ID_SHEET).execute()

            sheetList = self.connect.get('sheets')

        except Exception as es:
            print(f'🚫 Ошибка при подключении к Google таблицам "{es}"')

            return False

        try:

            name_list = [x['properties']['title'] for x in sheetList if x['properties']['title'] not in BLACK_NAME]

        except Exception as es:
            print(f'Ошибка при формирования списка имен вкладок "{es}"')

            return []

        return name_list

    @staticmethod
    def get_index_competitor(list_name_columns):
        ip_list_index = []
        for count, colm in enumerate(list_name_columns['values'][0]):

            _temp_ip = {}

            if 'Запрос' in colm:
                _temp_ip['name'] = colm
                _temp_ip['index'] = count

                ip_list_index.append(_temp_ip)

        return ip_list_index
