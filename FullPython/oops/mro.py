class A:
    label = "A: Base class"
class B(A):
    label = "B: Base class"
class C(A):
    label = "C: Base class"
    
class D(B,C):
    # label = "D: Base class"
    pass

cup = D()
print(cup.label)
print(D.__mro__)