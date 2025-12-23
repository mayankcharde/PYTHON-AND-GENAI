def pour_chai(n):
    print(n)
    if n==0:
        return "all cups poured"
    return pour_chai(n-1)
# mayank = pour_chai(3)
# print(mayank)
print(pour_chai(3))


#  THIS IS A LIST
chai_types = ["light", "kadak", "ginger", "kadak"]

#  WE ARE FILTERING HERE BY USING LAMDA EXPRESSION
#  AGAR KADAK PRESENT HAI TO WO FILTER HO JAYEGA AUR BAKI KI LIST SHOW HOGI  
strong_chai = list(filter(lambda chai:chai!="kadak", chai_types))
print(strong_chai)