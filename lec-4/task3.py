
month = int(input())

match month:
    case 12 | 1 | 2:
        season = "Зима ❄️"
    case 3 | 4 | 5:
        season = "Весна 🌸"
    case 6 | 7 | 8:
        season = "Лето ☀️"
    case 9 | 10 | 11:
        season = "Осень 🍂"

print(f"Месяц: {month}, сезон: {season}")
