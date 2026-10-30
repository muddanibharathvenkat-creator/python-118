food = float(input("Enter food expenses: "))
travel = float(input("Enter travel expenses: "))
hotel = float(input("Enter hotel expenses: "))
budget = float(input("Enter total budget: "))

total = food + travel + hotel

print("Total Expenses:", total)

if total <= budget:
    print("Within Budget")
else:
    print("Budget Exceeded by:", total - budget)