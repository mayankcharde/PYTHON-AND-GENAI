chai_menu = {"masala": 30, "ginger": 40}

try:
    chai_menu["elaichi"]
except KeyError:
    print(("the key that you are tying to access"))
    
print("hello code")       