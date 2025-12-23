order_amount = int(input("Enter the amount:"))

deilvery_fees =0 if order_amount >300 else 30

print(f"delivery fees is: {deilvery_fees}")