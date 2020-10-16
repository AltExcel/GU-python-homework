def my_math(a, b):
    while True:
        try:
            a = float(a)
            b = float(b)
            return a / b
        except ValueError:
            a = input("Введите числовое значение: ")
            b = input("Введите числовое значение: ")
        except ZeroDivisionError:
            a = input("Введите значение заново: ")
            b = input("Значение не может быт равно 0, введите значение заново: ")


print(my_math(input("Введите значение 1: "), input("Введите значение 2: ")))
print(my_math())
