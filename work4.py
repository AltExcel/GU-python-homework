
class Car:
    def __init__(self, name, colour, speed, is_police):
        self.Speed = speed
        self.Colour = colour
        self.Name = name
        self.Is_police = False if is_police == "нет" else True
        print(f"Автомобиль - {self.Name}, цвет - {self.Colour}, скорость - {self.Speed}",
              "Автомобиль принадлежит полиции" if self.Is_police is True else "")
        self.show_speed()

    def go(self, speed):
        self.Speed = speed
        print(f"Автомобиль {self.Name} движется со скоростью {self.Speed}")

    def stop(self):
        self.Speed = 0
        print(f"Автомобиль {self.Name} остановился")

    def turn(self, direction):
        print(f"Автомобиль {self.Name}, повернул {direction}")

    def show_speed(self):
        print(self.Speed)


class TownCar(Car):

    def show_speed(self):
        if int(self.Speed) > 60:
            print(f'Автомобиль {self.Name} превысил скорость!')
            print(
                f'Передвижение автомобиля со скоростью {self.Speed} запрещено.')
            self.Speed = 60


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if int(self.Speed) > 40:
            print(f'Автомобиль {self.Name} превысил скорость!')
            print(
                f'Передвижение автомобиля со скоростью {self.Speed} запрещено.')
            self.Speed = 40


class PoliceCar(Car):
    def turn_on_the_flashes(self):
        if self.Is_police:
            print('Мигалки включены')

    def turn_off_the_flashes(self):
        if self.Is_police:
            print('Мигалки выключены')

# Программа передвижения автомобилей
# Работа рабочей машины


work_car = WorkCar(name=input('Введите название машины: '),
                   colour=input('Введите цвет машины: '),
                   speed=input('Введите скорость: '),
                   is_police=input('Это полицейская машина? \nда нет: '))

work_car.go(50)
print("Текущая скорость -", work_car.Speed)
work_car.turn("Направо")
work_car.go(90)
print("Текущая скорость -", work_car.Speed)
work_car.stop()

# Работа спорткара
sport_car = SportCar(name=input('Введите название машины: '),
                     colour=input('Введите цвет машины: '),
                     speed=input('Введите скорость: '),
                     is_police=input('Это полицейская машина? \nда нет: '))

sport_car.go(100)
print("Текущая скорость -", sport_car.Speed)
sport_car.turn("Направо")
sport_car.go(90)
print("Текущая скорость -", sport_car.Speed)
sport_car.turn("Направо")
sport_car.stop()
print("Спорткар был остановлен")

# Работа полицейского автомобиля
police_car = PoliceCar(name=input('Введите название машины: '),
                       colour=input('Введите цвет машины: '),
                       speed=input('Введите скорость: '),
                       is_police=input('Это полицейская машина? \nда нет: '))

police_car.go(50)
police_car.turn_on_the_flashes()
print("Автомобиль преследует спорткар.")
print('Текущая скорость -', police_car.Speed)
police_car.turn('Направо')
police_car.go(100)
print('Текущая скорость -', police_car.Speed)
police_car.stop()
police_car.turn_off_the_flashes()

town_car = TownCar(name=input('Введите название машины: '),
                   colour=input('Введите цвет машины: '),
                   speed=input('Введите скорость: '),
                   is_police=input('Это полицейская машина? \nда нет: '))

town_car.go(50)
print("Текущая скорость -", town_car.Speed)
town_car.turn("Направо")
town_car.stop()
