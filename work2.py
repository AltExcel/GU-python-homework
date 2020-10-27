
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 40
        self.height = 8

    def mass_func(self):
        mass_func = self._length * self._width * self.weight * self.height
        print(f"Для полного покрытия дороги достаточно {mass_func}т асфальта")


roadmap = Road(5000, 18)
roadmap.mass_func()
