# Метод решения через список#
m0nts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
num = (int(input("Введите номер месяца: ")))
cancer = m0nts.count(num)

if cancer == 1:
    ben = m0nts.index(num)
    if ben >= 0 and ben <= 1 or ben == 11:
        print('Зима')
    elif ben >= 2 and ben <= 4:
        print('Весна')
    elif ben >= 5 and ben <= 7:
        print('Лето')
    elif ben >= 8 and ben <= 10:
        print('Осень')
    else:
        print("Введите корректные данные")
else:
    print("Введите корректные данные")

# Метод решения через словарь#
months = {(1, 2, 12): "Зима", (3, 4, 5): "Весна", (6, 7, 8): "Лето", (9, 10, 11): "Осень"}
zen = (int(input("Введите номер месяца: ")))
for el in months.keys():
    for a in el:

        if a == zen and zen >=1 and zen <=2 or zen == 12:
            print("Зима")
        elif a == zen and zen >=3 and zen <=5:
            print("Весна")
        elif a == zen and zen >=6 and zen <=8:
            print("Лето")
        elif a == zen and zen >= 9 and zen <= 11:
            print("Осень")
        else:
            print("Ошибка")






