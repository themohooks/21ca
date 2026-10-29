temperature = float(input("Введите температуру: "))
pressure = int(input("Введите верхнее давление: "))
pulse = int(input("Введите пульс: "))

if temperature < 35 or temperature > 38 or pressure < 105 or pressure > 140 or pulse < 55 or pulse > 110:
    print("Требуется врач")
elif temperature < 36 or temperature > 37 or pressure < 110 or pressure > 130 or pulse < 60 or pulse > 100:
    print("Легкое недомогание")
else:
    print("Нормальное состояние")