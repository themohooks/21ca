age = int(input("Введите возраст: "))
doc = input("Есть ли у вас документ? (да/нет): ").lower()
club_member = input("Вы член клуба? (да/нет): ").lower()

if (doc == "да" and age > 18) or club_member == "да":
    print("Добро пожаловать в клуб!")
else:
    print("Вход запрещён!")



