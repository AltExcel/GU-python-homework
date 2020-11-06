class Quest:
    def __init__(self):
        self.my_list = []

    def my_input(self):
        while True:
            val = input('Введите значения через пробел или stop для остановки программы и нажмите Enter:  ')
            if val == "stop":
                return f'Вы вышли'
            self.my_list.append(val)
            print(f'Текущий список - {self.my_list} \n ')
            val1 = val.split()
            val2 = []
            for doll in val1:
                try:
                    val2.append(int(doll))
                except ValueError:
                    print("Недопустимое значение: ", doll)
            print("Числовые значения: ", val2)


try_except = Quest()
print(try_except.my_input())
