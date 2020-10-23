import json
wonderland = open("work7test.txt", encoding="utf-8")

total_profit = 0
companies_num = 0
companies = wonderland.readlines()
profit_list = {}
average_profit = {}
for zen in companies:
    companies_list = zen.split()
    company, etc, revenue, cost = companies_list
    decision = int(revenue) - int(cost)
    profit_list[company] = decision
    if decision >= 1:
        total_profit = total_profit + decision
        companies_num += 1


def profit_func():
    return total_profit / companies_num


answer = profit_func()
average_profit["average profit: "] = answer
answer_list = []
answer_list.append(profit_list)
answer_list.append(average_profit)
print(answer_list)

with open("work7test.json", "w") as write_json:
    json.dump(answer_list, write_json)

