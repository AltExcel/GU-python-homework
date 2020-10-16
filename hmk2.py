
def info(**kwargs):
    listinfo = []
    for values in kwargs.values():
        listinfo.append(values)
    return listinfo


print(info(name=input("Введите имя: "), name2=input("Фамилию: "),
           bYear=int(input("Год рождения: ")), rescity=input("Город проживания: "),
           email=input("Email: "), pnumber=int(input("Номер телефона: "))))
