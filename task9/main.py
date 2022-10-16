salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев


def live(need_money, salary, spend, increase, months):
    liv = 0
    i = 0
    while i != months:
        liv = liv + salary - spend
        spend = spend + spend * increase
        i = i + 1
        need_money = int(-liv)
    print(need_money)
    return need_money


# TODO Оформить решение
live(need_money, salary, spend, increase, months)
