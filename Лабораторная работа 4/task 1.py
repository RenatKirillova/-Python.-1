# TODO решите задачу
import json  # Импорт модуля для работы с JSON данными
def task() -> float:
    with open("input.json", "r") as file:
        data = json.load(file)
    return round(sum(item.get("score", 0) * item.get("weight", 0) for item in data), 3)

print(task())

