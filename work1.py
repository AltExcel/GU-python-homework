from time import sleep
from itertools import cycle


class TrafficLight:

    __colour = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        worktime = 0
        for zen in cycle(TrafficLight.__colour):
            if zen == "Красный":
                print(zen)
                sleep(7)
            elif zen == "Желтый":
                print(zen)
                sleep(2)
            elif zen == "Зеленый":
                print(zen)
                sleep(8)
            if worktime > 3:
                print("Work end")
                break
            worktime += 1


light = TrafficLight()
light.running()
