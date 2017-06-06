print("Set")
s = {2, 1, 3, 4}
print(s)
print(type(s))

print("Empty set")
s = set()
print(s)

print("Set constructor")
print("Constructing set from a list")
s = set([1, -1, 4])
print(s)

print("Sets remove duplicate elements")
s = set([1, 1, 1, 1, 2])
print(s)

print("Iterating through set")
# Note order is arbitrary
for i in {1, 2, 3, 4, 5}:
    print(i)
    
# Membership operator
print("Membership operator")
print(1 in {1, 2, 3, 4, 5})
print(1 not in {1, 2, 3, 4, 5})

# adding element into set
print("adding element into set")
s = {1, 2}
print(s)
s.add(3)
print(s)
# Adding an element that already exists has no effect, and neither does it produce an error
s = {1, 2}
s.add(1)
print(s)

# Multiple elements can be added in one go using updated method
s = {1, 2}
s.update({3, 4})
print(s) 

# delete element from a set
print("Delete element in a set")
s = {1, 2}
s.remove(1)  # This can lead to error when there is not element
print(s)

print("Delete element in a set with out error")
s = {1, 2}
s.discard(3)  # This will not lead to any error
print(s)

# Copying sets
print("Copying sets, its a shallow copy")
s = {1, 2}
s1 = s.copy()
s2 = set(s)
print("s", s)
print("s1", s1)
print("s2", s2)

# Liner algebra
print("Set operations")
s1 = {1, 2}
s2 = {1, 4}
print("s1 intersection s2", s1.intersection(s2))
print("s1 union s2", s1.union(s2))
