actual_cost=float(input("Enter Actual Cost of Product: "))
selling_cost=float(input("Enter Selling Cost of Product: "))

if actual_cost > selling_cost:
    amt = actual_cost - selling_cost
    print("Total Loss is : ",amt)
elif actual_cost < selling_cost:
    amt = selling_cost - actual_cost
    print("Total Profit is : ",amt)
else:
    print("No Profit No Loss!")
