def process_order(item, quantity):
    try:
        price = {"masala":20}[item]
        cost = price*quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("sorry that chai is not on menu") 
    except TypeError:
        print("quantity must be in numbers")
    
process_order("ginger", 2)               
process_order("masala", 20)               
process_order("lemon", "two")               