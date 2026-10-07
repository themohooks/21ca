import math


def calculate_rectangle_area(width, height):
    """Рассчитывает площадь прямоугольника."""
    return width * height


def calculate_circle_area(radius):
    """Рассчитывает площадь круга."""
    return math.pi * radius ** 2


width, height = map(float, input("Введите ширину и высоту прямоугольника через пробел: ").split())

rectangle_area = calculate_rectangle_area(width, height)

print(f"Площадь прямоугольника: {rectangle_area:.2f}")

radius = float(input("Введите радиус круга: "))

circle_area = calculate_circle_area(radius)

print(f"Площадь круга: {circle_area:.2f}")