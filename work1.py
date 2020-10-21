from sys import argv


def milk():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Сумма к выплате: {time * rate + bonus}")
    except ValueError:
        print("Введите все необходимые данные.")


milk()
