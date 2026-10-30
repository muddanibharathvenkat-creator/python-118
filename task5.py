usage = float(input("Enter data usage in GB: "))

plan_a = 199 if usage <= 10 else 199 + (usage - 10) * 20
plan_b = 299 if usage <= 20 else 299 + (usage - 20) * 15

print("Plan A Cost:", plan_a)
print("Plan B Cost:", plan_b)

if plan_a < plan_b:
    print("Plan A is cheaper")
elif plan_b < plan_a:
    print("Plan B is cheaper")
else:
    print("Both plans cost the same")