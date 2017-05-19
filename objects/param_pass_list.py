def modify(y):  # y contains copy of reference x
    y.append(4)  # y refer to same object as x 
    print("y=", y)
x = [1, 2, 3]
print("x=", x)
modify(x)
print("x=", x)
