print("1. Конвертировать мили в час в км/ч")
print("2. Конвертировать км/ч в мили в час")

choice = int(input("Введите ваш выбор: "))

if choice == 1:
    mph = float(input("Введите скорость в милях в час: "))
    kph = mph * 1.60934
    print("{:.2f} миль/ч = {:.2f} км/ч".format(mph, kph))
elif choice == 2:
    kph = float(input("Введите скорость в км/ч: "))
    mph = kph / 1.60934
    print("{:.2f} км/ч = {:.2f} миль/ч".format(kph, mph))
else:
    print("Некорректный выбор")
