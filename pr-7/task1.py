print("⭐ РЕЙТИНГ ПРОДУКТА ⭐")

rating = int(input("Введите рейтинг от 1 до 10: "))

match rating:
    case 9 | 10:
        description = "Отличный 🤩"
        recommendation = "Рекомендую!"
    case 7 | 8:
        description = "Хороший 😊"
        recommendation = "Рекомендую!"
    case 4 | 5 | 6:
        description = "Средний 😐"
        recommendation = "Можно попробовать."
    case 1 | 2 | 3:
        description = "Плохой 😞"
        recommendation = "Не рекомендую."
    case _:
        description = None

if description is None:
    print("❌ Ошибка! Введите число от 1 до 10.")
else:
    print("\n--- Результат ---")
    print(f"Рейтинг: {rating}/10")
    print(f"Описание: {description}")
    print(f"Рекомендация: {recommendation}")
    

