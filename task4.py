basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentive = float(input("Enter incentive: "))

gross_salary = basic + allowance + overtime + incentive
deduction = gross_salary * 0.10
net_salary = gross_salary - deduction

print("Gross Salary:", gross_salary)
print("Deduction:", deduction)
print("Net Salary:", net_salary)