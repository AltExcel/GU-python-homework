print("У меня нету идей, что здесь можно придумать.")
z = int(input("Поэтому просто введите число, чтобы случилась магия: "))
zz = int(f"{z}{z}")
zzz = int(f"{z}{z}{z}")
answer = z + zz + zzz

print(f"{z}+{zz}+{zzz}=", answer)
print(f"Лучшее число на свете это {answer}.")
