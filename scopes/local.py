def fun():
    i = 10  # local scope
    print("i=", 10)

fun()
print(i)  # this leads to error because i is local scope
