import random
arctur = open("work5test.txt", "w", encoding="utf-8")

num_list = [random.randint(1, 51) for zen in range(1, 21)]
str_num = ' '.join(map(str, num_list))
arctur.writelines(str_num)

arctur.close()

arctur = open("work5test.txt", encoding="utf-8")

numbers = arctur.read()
sum_list = []
for num in numbers.split():
    sum_list.append(int(num))
print("Случайные числа: ", numbers)
print("Сумма чисел: ", sum(sum_list))

arctur.close()
