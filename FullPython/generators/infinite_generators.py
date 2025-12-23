def infinite_chai():
    count =1
    while True:
        yield f"refil #{count}"
        count+=1
        
refill = infinite_chai()  
print(refill)      
# print(next(refill))
# print(next(refill))
# print(next(refill))

user2 = infinite_chai()

for _ in range(5):
    print(next(refill))
    
for _ in range(6):
    print(next(refill))    
    