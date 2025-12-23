class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


#  HERE WE DONE INHERITANCE 
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        #  HERE WE CALLED PARENT CLASS CONSTRUCTOR
        super().__init__(type_, strength)
        self.spice_level = spice_level