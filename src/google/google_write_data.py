from settings import ID_SHEET
from src.google._slovar import colums_slovar


class GoogleWriteData:
    def __init__(self, google_core):
        self.google_core = google_core
        self.service = google_core.service

    def write_data(self, job):
        try:
            self.service.spreadsheets().values().batchUpdate(
                spreadsheetId=ID_SHEET,
                body={
                    "valueInputOption": "USER_ENTERED",
                    "data": [
                        {"range": f"{job['name_sheet']}!{job['price_index']}:{job['price_index']}",
                         "majorDimension": "COLUMNS",
                         "values": [[job['price']]]}
                    ]
                }
            ).execute()
        except Exception as es:

            print(f'Ошибка при изменение Google таблицы "{es}"')

            return False

        return True


if __name__ == '__main__':
    from src.google.google_modul import GoogleModul

    dir_project = 'C:\\Users\\user\\PycharmProjects\\ozon_google'

    google_core = GoogleModul(dir_project).connect_sheet()

    rows = {'competitor': 'Конкурент 1',
            'link': 'https://www.ozon.ru/product/zagustitel-agar-agar-900-blyum-komplekt-200-gr-proffi-naturalnyy-rastitelnyy-analog-zhelatina-897729039/?advert=ceEuSJStsVDwl0YTt251E777Q6zxS1TGi7dLjv4y6B8Se6EQ9WRJYhOUTb4qWvtvProoxq1aZAf13vhZSjnVQFATa1oNusOXjWYle4txTngDHo7V8GzOgVff6ggRn0DWBuYDJ8HTd5mkz8pDjlXeSnaB7CV8vFCdDSXMdQkxNKwEhqwWyBPdQwCCJDvbfMgmtq2BilBHawjysQBTABMc1EdteVGc5t271YoSMGFBIWrhmzTpTQROpT5kcR-0kN45ZLq150q6u6EVRWeA0NbTXThERZR4ZVrqqn7AtGvlDL3Dcktml4O4lL6XVvhEausIi-ZFxXTM2jTsm3Amu6UhMdoOb0QBwkbRNw&avtc=1&avte=2&avts=1689859430&keywords=агар+агар&sh=Hz4owRt9pA',
            'name_sheet': 'GF', 'x': 7, 'y': 'H3', 'price_index': 'I3', 'price': 1231234}

    change_core = GoogleWriteData(google_core).write_data(rows)

    print()
