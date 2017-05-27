i = 10  # global scope
def fun1():
    print("fun1 i=", i)
def fun2():
    print("fun2 i=", i)
fun1()
fun2()