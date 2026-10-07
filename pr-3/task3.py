try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    result = num1 + num2

    print("Сумма чисел:", result)

except ValueError:
    print("Ошибка! Введите целые числа.")