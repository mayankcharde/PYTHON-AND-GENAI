class chaiOrder:
    
    def __init__(self , type_, size):
        self.type_ = type_
        self.size = size
        
    def summary(self):
        return f"{self.size}ml of {self.type_} chai"
    
order = chaiOrder("masala", 200)
print(order.summary())


order_two = chaiOrder("ginger", 220)
print(order_two.summary())        
