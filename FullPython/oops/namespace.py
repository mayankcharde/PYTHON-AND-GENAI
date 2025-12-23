class chai:
    origin ='India'
    
print(chai.origin)

chai.is_hot =True
print(chai.is_hot)
   
masala = chai()
print(f"masala {masala.origin}")
print(f"masala {masala.is_hot}")
masala.is_hot = False

print("class:" , chai.is_hot)    
print("masala:" , masala.is_hot)
masala.flavour = "masala"
print(masala.flavour)    
