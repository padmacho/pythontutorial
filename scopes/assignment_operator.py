a = 0

def fun1():
    print("fun1: a=", a)
def fun2():
    a = 10  # By default, the assignment statement creates variables in the local scope
    print("fun2: a=", a)
def fun3():
    global a  # refer global variable
    a = 5
    print("fun3: a=", a)
    
fun1()
fun2()
fun1()
fun3()
fun1()
