# TODO Напишите функцию find_common_participants
def find_common_participants(participants1, participants2, separator=","):
    set1 = set(participants1.split(separator))
    set2 = set(participants2.split(separator))
    common_participants = sorted(list(set1.intersection(set2)))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
