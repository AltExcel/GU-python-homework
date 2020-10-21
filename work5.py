from functools import reduce

bird_list = [zen for zen in range(100, 1001) if zen % 2 == 0]


def plus_func(prev_el, el):
    return prev_el*el


print(reduce(plus_func, bird_list))
