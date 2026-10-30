distance = float(input("Enter distance in km: "))
age = int(input("Enter passenger age: "))

fare = distance * 2

if age < 12:
    fare *= 0.5
elif age >= 60:
    fare *= 0.7

fare += 30
print("Total Railway Fare:", fare)