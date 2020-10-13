number = int(input("Введите натуральное число: "))
rating = [9, 6, 4, 3, 1]
b = 0
for num in rating:
    if number >= num:
        rating.insert(b, number)
        break
    else:
        b += 1
print(rating)
