
def num_gen(number):
    m_num = 1
    if number == 0:
        yield f"{number}! = 1"
    for zen in range(1, number + 1):
        m_num *= zen
        yield f"{zen}! = {m_num}"


for elem in num_gen(int(input("Факториальное число:"))):
    print(elem)
