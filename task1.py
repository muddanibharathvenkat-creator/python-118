marks = float(input("Enter marks percentage: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter family income: "))

if marks >= 80 and attendance >= 75 and income <= 200000:
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")