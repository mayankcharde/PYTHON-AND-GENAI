def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

orders = [100,150,200]

for place in orders:
    #  HERE IN PRICES AS ARG WE PASSED ORDERS AS LIST
    final_amount = add_vat(place , 10)
    print(f"original: {place}, final with vat: {final_amount}")