# Scalar types are immutables
x = "abc"
y = "abc"
print("x==y", x == y)
print("x is y", x is y)
# Collections are mutable
x = ["a", "b", "c"]
y = ["a", "b", "c"]
print("x==y", x == y)
print("x is y", x is y)
