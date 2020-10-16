def elem(*args):
    zn = list(args)
    delt = min(zn)
    zn.remove(delt)
    return f"Ваш ответ: {sum(zn)}"


print(elem(int(input("Введите первое число: ")), int(input("Введите второе число: ")),
           int(input("Введите третье число: "))))
