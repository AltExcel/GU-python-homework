
def milk(x, y):
    while type(x) is str or type(y) is str:

        if type(x) is str:
           x = int(input("Ошибка значения. Введите положительное число: "))
        if type(y) is str:
           y = int(input("Ошибка значения. Введите отрицительную степень: "))

    while x < 1 or y > -1:

        if x < 1:
            x = int(input("Ошибка значения. Введите положительное число: "))
        if y > -1:
            y = int(input("Ошибка значения. Введите отрицительную степень: "))

    return x ** y


print(milk(input("Введите положительное число: "), input("Введите отрицательную степень: ")))
