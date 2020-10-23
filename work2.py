
poet_obj = open("work2text.txt", "r", encoding="utf-8")
lines = poet_obj
num_line = 1
for zen in lines:
    word = 0
    bell = zen.split()
    num_line += 1
    for words in bell:
        word_in_line = bell.count(words)
        word = word+word_in_line
    print(f"Количество слов в строке №{num_line} = {word}")


poet_obj.close()

print("Количество строк равно ", sum(1 for line in open("work2text.txt")))

