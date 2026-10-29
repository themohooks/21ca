import math


def calculate_distance(point_a, point_b):
    x_a, y_a = point_a
    x_b, y_b = point_b

    dx = x_a - x_b
    dy = y_a - y_b

    return math.sqrt(dx ** 2 + dy ** 2)


point_a = map(float, input("Введите x и y первой точки: ").split())
point_b = map(float, input("Введите x и y второй точки: ").split())

point_a = tuple(point_a)
point_b = tuple(point_b)

result = calculate_distance(point_a, point_b)

print(f"Евклидово расстояние: {result:.2f}")



