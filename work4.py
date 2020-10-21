import random

bird_list = [random.randint(1, 24) for _ in range(16)]
no_bird_list = [zen for zen in bird_list if bird_list.count(zen) == 1]
print(f"Сгенерированный список: {bird_list}\nСписок без повторений: {no_bird_list}")
