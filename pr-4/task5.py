BILLS = [5000, 2000, 1000, 500, 200, 100]


def calculate_bills(amount):
    """Рассчитывает количество купюр каждого номинала для выдачи."""
    result = {}

    for bill in BILLS:
        count = amount // bill
        result[bill] = count
        amount %= bill

    return result


amount = int(input("Введите сумму для снятия: "))

bills = calculate_bills(amount)

print("Отчет о выдаче:")

for bill, count in bills.items():
    if count > 0:
        print(f"Купюр {bill} руб.: {count} шт.")