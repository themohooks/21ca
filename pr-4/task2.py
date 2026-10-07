def calculate_bmi(weight, height):
    """Рассчитывает индекс массы тела."""
    return weight / (height * height)


weight, height = map(float, input("Введите вес (кг) и рост (м) через пробел: ").split())

bmi = calculate_bmi(weight, height)

print(f"Ваш ИМТ: {bmi:.1f}")