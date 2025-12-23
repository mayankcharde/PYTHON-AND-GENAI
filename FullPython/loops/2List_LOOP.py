names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]


#  BASICALLY ZIP IS THE METHOD IN WHICH WE CAN APPLY LOOP IN 2 LISTS OR TUPLES ALSO 
for name , amount in zip(names , bills):
    print(f"{name} paid {amount} rupees")