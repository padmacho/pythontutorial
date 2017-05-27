def outer():
    i = 10
    def inner():
        print("inner i=", i)    
    inner()
    print("Outer i=", i)

outer()
