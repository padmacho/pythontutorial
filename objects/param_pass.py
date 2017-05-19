def modify(y):
    y = y + 1  # integer objects are immutable.Now object get created and reference is assigned to y
    print("y=", y)
x = 20
print("x= ", x)
modify(x)
print("x=", x)
