money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить


def live(money_capital, salary, spend, increase, month):
    liv = 0
    sp = spend
    while money_capital > spend:
        liv = money_capital + salary - spend

        spend = spend * (increase + 1)
        money_capital = liv
        month = month + 1

    print(month)
    return month


# TODO Оформить решение
live(money_capital, salary, spend, increase, month)
