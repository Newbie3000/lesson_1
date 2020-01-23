print("Task 5")
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
revenue = int(input("Enter revenue: "))
costs = int(input("Enter costs: "))
if revenue > costs:
    profitability = revenue - costs
    print(f"Great work. You have {profitability} profitability")
    worker = int(input("How many people work: "))
    print(f"{profitability / worker} for one worker")
elif revenue == costs:
    print("No bad")
else:
    print("Good luck")
