print("☕ МЕНЮ КАФЕ")

print("1. Кофе — 150 руб.")
print("2. Чай — 100 руб.")
print("3. Латте — 200 руб.")
print("4. Сок — 120 руб.")
print("5. Лимонад — 130 руб.")

drink = input("Выберите напиток (номер или название): ")

match drink:
    case "1" | "кофе":
        name = "Кофе"
        price = 150
    case "2" | "чай":
        name = "Чай"
        price = 100
    case "3" | "латте":
        name = "Латте"
        price = 200
    case "4" | "сок":
        name = "Сок"
        price = 120
    case "5" | "лимонад":
        name = "Лимонад"
        price = 130
    case _:
        name = None

if name is None:
    print("❌ Такого напитка нет!")
else:
    try:
        count = int(input("Введите количество порций: "))

        if count <= 0:
            print("❌ Количество должно быть больше нуля!")
        else:
            code = input("Введите код скидки (или Enter): ")

            match code:
                case "CAFE10":
                    discount = 10
                case "CAFE20":
                    discount = 20
                case _:
                    discount = 0

            total = price * count
            final_price = total - total * discount / 100

            match count:
                case 1:
                    word = "порция"
                case 2 | 3 | 4:
                    word = "порции"
                case _:
                    word = "порций"

            print("\n--- 🧾 ЧЕК ---")
            print(f"Напиток: {name}")
            print(f"Цена за порцию: {price} руб.")
            print(f"Количество: {count} {word}")
            print(f"Сумма: {total} руб.")
            print(f"Скидка: {discount}%")
            print(f"К оплате: {final_price:.2f} руб.")

            if code != "" and discount == 0:
                print("⚠️ Промокод не действует.")

    except ValueError:
        print("❌ Введите количество целым числом!")