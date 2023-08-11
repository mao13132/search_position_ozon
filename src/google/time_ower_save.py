from datetime import datetime

from settings import ID_SHEET


class TimeOwerSave:
    def __init__(self, google_core):
        self.google_core = google_core
        self.service = google_core.service

    def get_all_title(self):

        try:

            self.values = self.service.spreadsheets().values().get(
                spreadsheetId=ID_SHEET,
                range=f'Индексы!F1:F14',
                majorDimension='COLUMNS'
            ).execute()

        except Exception as es:
            print(f'🚫 Ошибка при TimeOwerSave get_all_title таблицам "{es}"')

            return False

        return self.values

    @staticmethod
    def get_index_my_title(list_name_title, my_title):
        for count, colm in enumerate(list_name_title['values'][0]):

            _temp_ip = {}

            if my_title in colm:
                return count + 1

        print(f'Ошибка, нет строчки в индексах для сохранения результата')

        return False

    def write_ower_save(self, _index, _time):
        try:
            self.service.spreadsheets().values().batchUpdate(
                spreadsheetId=ID_SHEET,
                body={
                    "valueInputOption": "USER_ENTERED",
                    "data": [
                        {"range": f"Индексы!H{_index}:H{_index}",
                         "majorDimension": "ROWS",
                         "values": [[_time]]}
                    ]
                }
            ).execute()
        except Exception as es:

            print(f'Ошибка при write_ower_save таблицы "{es}"')

            return False

        return True

    def write_time(self, my_title):
        all_title = self.get_all_title()

        if not all_title:
            return False

        index_my_title = self.get_index_my_title(all_title, my_title)

        if not index_my_title:
            return False

        time_ = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        res_write_time = self.write_ower_save(index_my_title, time_)

        return res_write_time
