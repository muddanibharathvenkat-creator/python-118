price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total >= 2000:
    discount = total * 0.10
else:
    discount = 0

tax = (total - discount) * 0.05
final_amount = total - discount + tax

print("Total:", total)
print("Discount:", discount)
print("Tax:", tax)
print("Final Amount:", final_amount)