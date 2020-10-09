que = int(input("Введите нужное Вам число "))
maxnumber = que % 10
while que >= 1:
    que = que // 10
    if que % 10 > maxnumber:
        maxnumber = que % 10
    if que > 9:
        print(maxnumber)
        continue
    else:
        break
print("Самая большая цифра в Вашем числе это", maxnumber)
