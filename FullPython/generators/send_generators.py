def chai_customer():
    print("welcome")
    order = yield
    while True:
        print(f"preparing: {order}")
        order = yield
        
stall = chai_customer()
next(stall)

stall.send("masala chai")        
stall.send("lemon chai")        