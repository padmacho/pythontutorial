capitals = {"india":"delhi", "america":"washington"}
print("Access values using key: ", capitals["india"])

name_age = [('dora', 5), ('mario', 10)]
d = dict(name_age)
print("Dict", d)
d = dict(a=1, b=2, c=3)
print("Dict", d)

# copying method 1
e = d.copy()
print("Copied dictionary e: ", e)

# copying method 2
f = dict(d)
print("Copied dictionary f: ", f)

# updating dict
g = dict(a=-1, b=-2)
print("d", d)
print("g", g)
d.update(g)
print("Updated dictionary d with g", d)

# Iterating through dictionary
d = dict(a=1, b=2, c=3)
# Note key are retrieved in arbitrary order
for key in d:
    print(d[key]) 

# iterate through values
# There is no efficient way to get keys from values
print("Get values for dictionary with out keys")
for value in d.values():
    print(value) 

print("Get items for dictionary")
# Each key-value pair in a dictionary is called an item, and we can get ahold of an iterable view of the items using the items() dictionary method.
for key, value in d.items():
    print(key, value)

# member ship operator works only on keys
d = dict(a=1, b=2, c=3)
print("a" in d)
print("e" in d)

# Remove an item from the dictionary
d = dict(a=1, b=2, c=3)
print("d", d)
print("Removing item c from dictionary")
del d['c']
print(d)

# Keys are immutable and values can be modified
d = dict(a=1, b=2, c=3)
print("d", d)
print("Modify element value of item a")
d["a"] = -1
print("d", d)

# Pretty printing
print("Pretty printing")
from pprint import pprint as pp
d = dict(a=1, b=2, c=3)
pp(d)



    
