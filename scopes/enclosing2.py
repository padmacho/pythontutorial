def outer():
    i = 10
    def inner():
        nonlocal i
        i = 30  #This will refer outer i
        print("inner i=", i)    
    inner()
    print("Outer i=", i)

outer()
