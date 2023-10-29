price = 0
tickets = (int(input("Укажите количество билетов:")))
for age in range (tickets):
    age = (int(input("Укажите ваш возраст:")))
    if age < 18:
        price += 0
    elif age >= 18 and age <= 25:
        price += 990
    elif age > 25:
        price += 1390
if tickets > 3:
    price -= price / 100 * 10
print ("Стоимость билетов:", price)
