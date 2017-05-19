def modify(y):  # y contains copy of reference x
    y = [1, 2, 3, 4]  # a new list object is created and assigned to y 
    print("y=", y)
x = [1, 2, 3]
print("x=", x)
modify(x)
print("x=", x)
