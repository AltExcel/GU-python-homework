
you_list = [200, 34, 11, 15, 22, 19, 2, 34, 44, 1, 52]

why_more = [you_list[num] for num in range(1, len(you_list)) if you_list[num] > you_list[num - 1]]
print(why_more)
