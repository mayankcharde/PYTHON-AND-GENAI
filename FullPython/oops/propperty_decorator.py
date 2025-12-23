class TeaLeaf:
    def __init__(self, age):
        self._age = age
        
    @property
    #  THIS IS BASICALLLY A GETTER 
    def age(self):
        return self._age + 2
    
    @age.setter
    #  THIS IS A SETTER 
    def age(self, age):
        if 1<= age <= 5:
            self._age = age
        else:
            raise ValueError("tea leaf is insufficient")
        
        
leaf = TeaLeaf(2)
print(leaf)
leaf.age = 6
print(leaf.age)       