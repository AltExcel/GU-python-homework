# ---------------------------------------скрипт №1-------------------------------------------------#
from itertools import count

for nor in count(9):
    if nor > 36:
        break
    else:
        print(nor)


print("=========================")
# ---------------------------------------скрипт №2-------------------------------------------------#

from itertools import cycle

zen = 1
for north in cycle([3, 5, 4, 99, 25, 55]):
    if zen > 18:
        break
    print(north)
    zen += 1
