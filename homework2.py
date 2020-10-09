print("Добро пожаловать! Спасибо, что решили воспользоваться нашим конвертером")
time = int(input("Введите время: "))
hours = (time // 3600)
minutes = (time // 60)
while minutes >= 60:
    minutes -= 60
seconds = time
while seconds >= 60:
    seconds -= 60
print(f"Время составляет {hours}ч{minutes}м{seconds}с")
