#  THIS IS A LIST OF ELEMENTS 
menu = ["green", "lemon" , "spiced" , "mint"]

#  HERE WE APPLY FOR LOOP IN THE FORM OF ENUMERATE FUNCTION
# WE GIVE IDX=ID OF THE LOOP "START="" IS EXISTING FUNCTION IN ENUMERATE
for idx, item in enumerate(menu, start=1):
    
    print(f"{idx} : {item}")