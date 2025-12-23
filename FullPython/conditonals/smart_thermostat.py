device_status = "active"
temperature = 39

if device_status == 'active':
    if temperature > 35:
        print("high temp")
    else:
        print("low temp")    
else:
    print("device is offline")        