i = 10  # global scope
def fun1():
    print("fun1 i=", i)
def fun2():
    i = 20  # This will created a new local variable i 
    print("fun2 i=", i)
fun1()
fun2()
fun1()
