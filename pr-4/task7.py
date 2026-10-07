FUEL_PRICE_PER_LITER = 49.5
LITERS_PER_100_KM = 100


def calculate_fuel_cost(distance_km, fuel_consumption):
    """Рассчитывает количество топлива и стоимость поездки."""
    fuel_used = distance_km * fuel_consumption / LITERS_PER_100_KM
    total_cost = fuel_used * FUEL_PRICE_PER_LITER

    return fuel_used, total_cost


distance_km = float(input("Введите расстояние поездки (км): "))
fuel_consumption = float(
    input("Введите расход топлива на 100 км (л): ")
)

fuel_used, total_cost = calculate_fuel_cost(
    distance_km,
    fuel_consumption
)

print(f"\nРасход топлива: {fuel_used:.2f} л")
print(f"Стоимость поездки: {total_cost:.2f} руб.")