money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 1
current_money = money_capital

while True:
    if current_money < spend:
        break

    months += 1
    current_money -= spend
    current_money += salary
    spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months)
