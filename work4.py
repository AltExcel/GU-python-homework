from googletrans import Translator

mantis = open("work4test.txt", "r+", encoding="utf-8")
nurse = open("work4test2.txt", "w", encoding="utf-8")
translator = Translator()
for zen in mantis:
    doll = zen.split()
    org = doll.pop(0)
    bang = []
    result = translator.translate(org, src="en", dest="ru")
    doll.insert(0, result.text)
    doll.append('\n')
    nurse.writelines(doll)
mantis.close()
nurse.close()


