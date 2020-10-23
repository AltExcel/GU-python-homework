
work_pay = open("work3test.txt", encoding="utf-8")
midpay = []
for zen in work_pay:
    doll = zen.split()
    pay = float(doll.pop(2))

    if pay <= 20000:
        print("Бедолага: ", doll.pop(0))
    midpay.append(pay)


def mind(midpay):
    return sum(midpay)/len(midpay)


answer = mind(midpay)
print(f"Средняя зарплата равна: {answer}")
