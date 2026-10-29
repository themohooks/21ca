number = int(input())

if number < 0 or number > 36:
    print("ошибка ввода")
elif number == 0:
    print("зеленый")
elif 1 <= number <= 10 or 19 <= number <= 28:
    if number % 2 == 1:
        print("красный")
    else:
        print("черный")
else:
    if number % 2 == 1:
        print("черный")
    else:
        print("красный")