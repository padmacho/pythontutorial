def modify(y):  # y contains copy of reference x
    y = None  # y is referring to NoneType but x reference is still alive 
    print("y=", y)
x = [1, 2, 3]
print("x=", x)
modify(x)
print("x=", x)
