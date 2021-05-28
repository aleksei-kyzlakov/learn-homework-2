import csv

"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

dict = [{"name":"Watson","age":20, "job":"Plumber"},
    {"name":"Johnson","age":30, "job":"Roofer"},
    {"name":"Andrews","age":40, "job":"Floorer"},
    {"name":"Peterson","age":50, "job":"Waller"},
    {"name":"Bjorn","age":60, "job":"Painter"},
    {"name":"Johanes","age":70, "job":"Officer"},
    {"name":"Holmes","age":80, "job":"Seargent"},
    {"name":"Stevens","age":90, "job":"Firefighter"},
    {"name":"Stephenson","age":100, "job":"Medic"},
    {"name":"Rogers","age":110, "job":"DPS"},
    {"name":"Bucky","age":120, "job":"Taunt"}
]


def main():
    with open("csv_test.csv", "w", encoding='utf-8', newline='') as file:
        fields = ["name", "age", "job"]
        writer = csv.DictWriter(file, fields, delimiter=';')
        # шапка таблицы writer.writeheader() 
        for row in dict:
            writer.writerow(row)


if __name__ == "__main__":
    main()
