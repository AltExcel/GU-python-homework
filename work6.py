
farida = open("work6test.txt", encoding="utf-8")
lesson = farida.readlines()
lesson_cake = {}
for zen in lesson:
    lesson_list = zen.split()
    less = sorted(lesson_list)
    numbers = 0
    for doll in less:
        if doll.isdigit() == True:
            numbers = numbers + int(doll)
        elif len(doll) >= 4:
            lesson_cake[doll] = numbers

print(lesson_cake)
