from datetime import datetime, timedelta

"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    print(datetime.today())
    print(datetime.today() - timedelta(days=1))
    print(datetime.today() - timedelta(days=30))


def str_2_datetime(date_string):
    date = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return date

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
