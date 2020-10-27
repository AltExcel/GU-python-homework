
class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        income_dict = {}
        income_dict["wage"] = int(input("Введите З/П: "))
        income_dict["bonus"] = int(input("Введите премию: "))
        self._income = income_dict


class Position(Worker):
    def get_full_name(self):
        print(f"Имя сотрудника: {self.name}, Фамилия: {self.surname}")

    def get_total_income(self):
        print("З/П сотрудника равна: ", sum(self._income.values()))


p = Position("Алексей", "Толстов", "Разработчик Python")
p.get_full_name()
p.get_total_income()
