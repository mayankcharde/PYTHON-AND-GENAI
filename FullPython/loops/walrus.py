# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")



value =13

#  THIS IS WALRUS OPERATOR 
#  THROUGH THIS WE CAN ALSO MAKE AND ADD IF CONDITION SIMENTANEOUSLY 
if remainder := value % 5:
    print(f"Not divisible, remainder is {remainder}")
        
        
        
        
        
flavors = ["masala", "ginger", "lemon", "mint"]
    
print("Available flavors: ", flavors)

#  IN THIS WE CAN ADD LOOPS AND MAKE USER INPUT BOTH THROUGH WALRUS OPERATOR 
while (flavor := input("choose your flavor:")) not in flavors:
    print(f" sorry ,  {flavor} is not available")
    
    #  THIS IS ELSE CONDITION 
print(f"you choose {flavor} chai")    