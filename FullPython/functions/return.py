def idle_chaiwala():
    pass

# IT WILL PRINT NONE
print(idle_chaiwala())

def sold_cups():
    return 120

total = sold_cups()
print(total)

def chai_status(cups_left):
    if cups_left ==0:
        return 'sorry'
    return 'chai is ready'
    
print(chai_status(0))
print(chai_status(5))


def chai_report():
    return 100,20,30
#  THIS ALL VARIABLES WILL ASSIGN THE ONE-ONE VALUES OF RETURN STATEMENT 
sold , remianing , not_paid = chai_report()
print("sold", sold)
print("remioaning" , remianing)
print("not_paid", not_paid)