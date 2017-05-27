def outer():
    i = 10
    def inner():
        i = 30  # This will create new local variable i instead of using outer i
        print("inner i=", i)    
    inner()
    print("Outer i=", i)

outer()
