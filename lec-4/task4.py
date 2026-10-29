
a = float(input())
op = input()
b = float(input())

match op:
    case "+":
        result = a + b
        print(f"{a} + {b} = {result}")
    case "-":
        result = a - b
        print(f"{a} - {b} = {result}")
    case "*":
        result = a * b
        print(f"{a} * {b} = {result}")
    case "/":
        if b == 0:
            print("Ошибка: деление на ноль.")
        else:
            result = a / b
            print(f"{a} / {b} = {result}")
    case _:
        print("Неизвестная операция.")
