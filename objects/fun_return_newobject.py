def modify(y):
    return [1, 2, 3]  # returns new object
x = [1, 2, 3]
y = modify(x)
print("x == y", x == y)
print("x == y", x is y)
