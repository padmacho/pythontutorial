i = 10  # global scope
def fun1():
    print("fun1 i=", i)
def fun2():
    global i  # This will refer to global variable i
    i = 20   
    print("fun2 i=", i)
fun1()
fun2()
fun1()
