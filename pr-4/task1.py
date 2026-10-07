TAX_RATE = 0.13


def calculate_tax(income):
    """Рассчитывает сумму подоходного налога."""
    return income * TAX_RATE


def calculate_net_income(income, tax):
    """Рассчитывает доход после вычета налога."""
    return income - tax


income = float(input("Введите годовой доход: "))

tax = calculate_tax(income)
net_income = calculate_net_income(income, tax)

print(f"Общая сумма дохода: {income:,.2f} руб.".replace(",", " "))
print(f"Сумма рассчитанного налога: {tax:,.2f} руб.".replace(",", " "))
print(f"Сумма «на руки»: {net_income:,.2f} руб.".replace(",", " "))