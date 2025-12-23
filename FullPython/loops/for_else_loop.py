staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name , age in staff:
    if age <=18:
        print(f"{name} is elegible to manage the staff")
        break
    
else:
    print(f"no one is eleigble")