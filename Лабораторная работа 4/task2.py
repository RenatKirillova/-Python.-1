
#Изначально при запуске, input.csv был пустым. не было возможности проверить работу кода. я внесла  исходные данные в csv из вкладки "compare Outputs"

import csv
import json
from collections import OrderedDict

def csv_to_json(csv_file_path, delimiter=','):
    with open(csv_file_path, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        return json.dumps([OrderedDict(row) for row in reader], indent=4)
#ранний вариант был с использованием data списка OrderedDict row позволило сократить код на пару строк
if __name__ == '__main__':
    csv_file = 'input.csv' # Указала имя CSV файла для обработки.
    json_output = csv_to_json(csv_file)
    print(json_output) # Вывод JSON данных в консоль
