def serve_chai():
    chai_type = "Masala"
    print(f"inside function {chai_type}")
    
    
chai_type = "lemon"
serve_chai()
print(f"outside function: {chai_type}")



#  OUTSIDE SCOPE OUTER SCOPE 
def chai_counter():
    chai_order = "lemon"
    #  INNER SCOPE INSIDE THE FUNCTION 
    def print_order():
        chai_order = "ginger"
        print(f"inner:" , chai_order)
    print_order()
    print(f"outer" , chai_order)
    
#  THIS IS GLOBAL SCOPE    # 
chai_order = "tulsi"
chai_counter()
print("global:" , chai_order)        