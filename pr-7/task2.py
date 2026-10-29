import random

print("📦 ОТСЛЕЖИВАНИЕ ЗАКАЗА")

status = input(
    "Введите статус (pending, processing, shipped, "
    "delivered, cancelled): "
)

match status:
    case "pending":
        name = "В ожидании ⏳"
        description = "Заказ ожидает обработки."
        days = random.randint(1, 3)

    case "processing":
        name = "В обработке ⚙️"
        description = "Заказ готовят к отправке."
        days = random.randint(2, 5)

    case "shipped":
        name = "Отправлен 🚚"
        description = "Заказ находится в пути."
        days = random.randint(1, 7)

    case "delivered":
        name = "Доставлен ✅"
        description = "Заказ получен."
        days = 0

    case "cancelled":
        name = "Отменён ❌"
        description = "Заказ отменён."
        days = 0

    case _:
        name = None

if name is None:
    print("❌ Неизвестный статус заказа!")
else:
    print("\n--- Информация о заказе ---")
    print(f"Статус: {name}")
    print(f"Описание: {description}")

    if days == 0:
        print("Время ожидания: не требуется")
    else:
        print(f"Примерное ожидание: {days} дн.")



        