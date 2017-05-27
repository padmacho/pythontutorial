def outer():
    def inner():
        i = 10
    inner()
    print("Outer i=", i) # this leads to error because variable in in inner function cannot be accessed out side

outer()
