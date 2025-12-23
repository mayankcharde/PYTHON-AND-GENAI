def chai_flavor(flavor="masala"):
    """ return the flavor of chai """
    chai = "ginger"
    return flavor

#  IT GIVES THE RETURN STATEMENT IN DOCSTRING 
print(chai_flavor.__doc__)
#  IT GIVES THE NAME OF THE FUNCTION 
print(chai_flavor.__name__)

# help(len)

#  HERE WE PASSES THE ARGS AS BY DEFAULT 0
def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa

    :param chai: Number of chai cups (10 rupees each)
    :param samosa: NUmber of samosa (15 rupees each)
    : return: (total amount, thank you message as string)
    """
    
    total = chai*10 + samosa*15
    return total, "thankyou"
    # print(f"return total",  total)

print(generate_bill(chai=1, samosa=2))