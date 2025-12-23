def server_chai():
    yield "cup1 :masala chai"
    yield "cup2 :ginger chai"
    yield "cup3 :elaichi chai"
    
stall = server_chai()  
print(next(stall))    
print(next(stall))    
print(next(stall))    

def get_chai_list():
    return ["cup1" ,  "cup2" , "cup3"]

def get_chai_gen():
    yield "cup1"
    yield "cup2"
    yield "cup3"
    
chai = get_chai_gen()
print(next(chai))    
print(next(chai))    
print(next(chai))    