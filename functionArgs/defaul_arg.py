
def add(x, y=0, z=0): 
    # x is called positional argument
    # y, z are called keyword argument
    print("x=", 10, "y=", y, "z=", z)
    return x + y + z
# add()  # This will result error because of missing positional argument: 'x'
add(10, 20)  # x is 10, y is 20
add(10)  # x is 10 
add(10, z=10)  # x is 10 and z is 10
# add(y=20)# This will result error  missing 1 required positional argument: 'x'

