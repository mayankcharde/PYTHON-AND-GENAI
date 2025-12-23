class baseChai:
    
    def __init__(self, type_):
        self.type = type_
        
    def prepare(self):
        print(f"preparing {self.type} chai")
        
class masalaChai(baseChai):
    def add_spices(self):
        print("adding cardmon spices")
        
        
        
class chaiShop:
    chai_cls = baseChai
    
    def __init__(self):
        self.chai = self.chai_cls("regular")  
        
    def serve(self):
        print(f"serving {self.chai.type} chai in the shop")
        self.chai.prepare()    
        
class fancyChaiShop(chaiShop):
        chai_cls = masalaChai
        
       
       
shop = chaiShop()
fancy = fancyChaiShop()
masala = masalaChai()
shop.serve()
fancy.serve()  
masala.prepare()      
