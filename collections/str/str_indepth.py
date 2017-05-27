# Length of the string
print("length: ", len("Hello World"))

# String concatenation using +
print("concatenation using + operator: ", "Hello" + "World")

# Join Method
print("Join method: ", "".join(["Hello" , "World"]))
print("Join with semicolon: ", ";".join(["Hello" , "World"]))

# split method
print("split by semicolon", "Hello;World".split(";"))

# partitioning
source, seperator, dest = "hyderbad:newyork".partition(":")
print("source, seperator, dest =", source, seperator, dest)

# Use format() to insert values into strings
print("Welcome to {0}".format("India"))
print("Welcome to {0},current temperature is {1} centigrade ".format("India", 30))
print("Welcome to {0}. I hope you like {0}".format("India"))

# If keyword arguments are supplied to formats, then named fields can be used instead of indexes.
print("Welcome to {country}".format(country="India"))

p = (10, 20, 30)
print("Coordinates x={point[0]},y={point[1]},z={point[2]}".format(point=p))

# We pass the whole math module to format using a keyword argument
import math
print("Math constants: pi={m.pi}, e={m.e}".format(m=math))

#Format strings also give us a lot of control over field alignment and floating point formatting.
print("Math constants: pi={m.pi:.3f}, e={m.e:.4f}".format(m=math))