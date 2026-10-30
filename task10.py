venue = float(input("Enter venue cost: "))
food = float(input("Enter food cost: "))
transport = float(input("Enter transport cost: "))
sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per student: "))

total_cost = venue + food + transport
remaining = total_cost - sponsorship

if remaining <= 0:
    students = 0
else:
    students = int(remaining / fee)
    if students * fee < remaining:
        students += 1

print("Total Event Cost:", total_cost)
print("Sponsorship:", sponsorship)
print("Minimum Students Required:", students)