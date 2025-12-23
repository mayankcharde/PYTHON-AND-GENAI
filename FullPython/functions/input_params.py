chai = [1,2,3]

def edit_chai(cup):
    cup[1] = 42
    
edit_chai(chai)
print(chai)    



def make_chai(tea, milk, sugar):
    print(tea, milk,sugar)
    

make_chai("Darjeeling", "Yes", "Low") #positional
make_chai(tea="Green", sugar="Medium", milk="No") #keywords


#  HERE WE SINGLE * WE PASSED ONLY ONE ARGS OR PARAMS AS INPUT
#  IN TWO ** WE PASSED VALUE ALSO PLUS ITS KEYS
def special_chai(*ingredients, **extras):
    print("ingri", ingredients)
    print("extras", extras)
    
special_chai("cinnamon", "cardmon" ,  sweetener="Honey", foam="yes")    


def chai_order(order=None):
    if order is None:
        order = []
    print(order)
    
chai_order()
chai_order()        


