PLACES_PER_KUPE = 4

place = int(input('Введите номер вагона: '))

kupe = (place - 1) // PLACES_PER_KUPE + 1

print('Ваш номер купе: ', kupe)


