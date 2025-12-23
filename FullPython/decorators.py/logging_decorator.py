from functools import wraps

def log_activity(func):
    wraps(func)
    
    def wrapper(*args,  **kwargs):
        print(f"calling: {func.__name__}")
        #  HERE WE ARE ACCCEPTING ARGS AND KWARGS
        result = func(*args, **kwargs)
        print(f" fininshed: {func.__name__}")
        return result
    return wrapper


@log_activity
#  PASSING ARGS AND KWARGS 
# IN KWARGS WE HAVE TO GIVE THE VALUE ALSO 
def brew_chai(type, milk="no"):
    print(f"brewing {type} chai and milk {milk}")
    
brew_chai("Masala")