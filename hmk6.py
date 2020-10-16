#не понимаю, как выполнить задание
def int_func(text):
    text = text.split()
    answer = ""
    for zen in text:
        for be in zen:
            if ord(be) < 97 or ord(be) > 122:
                text.remove(zen)
                break
        else:
            answer = answer + zen
    return answer.title()


print(int_func("nice авп ъghj jапро hjjпаро вапрghgh cool"))
