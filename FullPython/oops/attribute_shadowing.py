class chai:
    temp = "hot"
    strength = "strong"
    cup = "large"
    
cutting = chai()
print(cutting.temp)

cutting.temp = "mild"
cutting.cup = "small"
print("After changing ",cutting.temp)
print("cup size is  ",cutting.cup)
print("Direct look into the class ", chai.temp)

del cutting.temp
del cutting.cup
print(cutting.temp)
print(cutting.cup)