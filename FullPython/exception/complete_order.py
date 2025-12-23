class InvalidChaiError(Exception): pass


def bill(flavor, cups):
        menu = {"masala": 20, "ginger": 40}
        
        try:
            if flavor not in menu:
                raise InvalidChaiError("not available")
            if not isinstance(cups , int):
                raise TypeError("number of cups must be an integer")
            total = menu[flavor] * cups
            print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")
        except  Exception as e:
            print("error:" , e)
        finally:
            print("thankyou")
            
bill("mint", 2)                       
bill("ginger", 3)                       
bill("lemon","three")                       
bill("masala","three")                       
                    