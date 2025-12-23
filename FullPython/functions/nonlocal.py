#  THIS IS A GLOBAL SCOPE 
chai_type = 'ginger'

def update_order():
    # THIS IS A OUTER SCOPE 
    chai_type= 'elaichi'
    
    def kitchen():
        # WE MADE THIS NON-LOCAL
        nonlocal chai_type
        chai_type = 'kesar'
        #  THIS WILL PRINT ELAICHI BECAUSE IT IS IN THE FUNCTION
        # kitchen()
        
        #  THIS WILL RPINT KESAR BECAUSE IT IS OUT OF METHOD/FUNCTION
        #  THATS WHY WE MAKE KESAR NON-LOCAL 
    kitchen()    
    print("after kitchen update", chai_type)
    
update_order()        