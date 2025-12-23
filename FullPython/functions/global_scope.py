chai_type ="plain"

def front_desk():
    def kitchen():
        #  BECAUSE WE MAKE IT GLOBAL WE CAN ACCESS IT IN GLOBALLY
        global chai_type
        chai_type = "irani"
    kitchen()
    
    
    
front_desk()
print(f"final global chai:", chai_type)        