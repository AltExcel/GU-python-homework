#не понимаю, как выполнить задание

result = 0
while True:

    user_input = input("Введите числа через пробел: ")
    number, end = filter(user_input)
    number = number.split()
    res = 0

    while res < len(number):

        try:
            number[res] = int(number[res])
            res += 1
        except ValueError:
            print("Введите число или q: ")
    result += sum(number)
    print(f"Сумма равна {result} ")




