salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен


def calculate_required_money_capital(salary, spend, months, increase):
    required_money_capital = 0
    current_spend = spend

    for _ in range(months):
        current_spend *= (1 + increase)  # Увеличиваем расходы на инфляцию

        if salary < current_spend:
            required_money_capital += (current_spend - salary)  # Добавляем нехватку к подушке

    return int(required_money_capital + 0.99999999999999) # Округляю в большую сторону


required_capital = calculate_required_money_capital(salary, spend, months, increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_capital)

