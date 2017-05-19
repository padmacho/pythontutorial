def modify(y):
    return y  # returns same reference. No new object is created
x = [1, 2, 3]
y = modify(x)
print("x == y", x == y)
print("x == y", x is y)