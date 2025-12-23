from functools import wraps

#  HERE WE CREATE OUR CUSTOMIZE WRAPPER/DECORATOR 
def my_decorators(func):
    @wraps(func)
    
    def wrapper():
        print("before function runs")
        #  JIS FUNCTION ME HUM YE DECORAROR LAGAYEGA WO FUNC CHAL JAYEGA 
        func()
        print("after function runs")
    return wrapper

@my_decorators
def greet():
    print("hellp from decorators")
    
greet()
print(greet.__name__)        