import time
#The default argument expressions are evaluated only once when the def statement is executed
def show_time(arg=time.ctime()):
    print(arg)

show_time()# prints current time
time.sleep(5)# sleep for 5 sec
show_time()# prints current time
  
