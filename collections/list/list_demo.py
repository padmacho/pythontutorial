names = ["dora", "spider man ", "papa smurf", "captain america", "mario"]
# The first element of the sequence is at index 0
print("First element in the list", names[0])
print("First element in the list", names[-0])
# The last element of the sequence is at index -1
print("First element in the list", names[-5])


# Slicing is a form of extended indexing which allows us to refer to portions of a list
print("Slicing")
print("Get three elements from index 1", names[1:1 + 3])
print("Get all elements in the except first and last", names[1:-1])
print("Get all elements in the list", names[0:])
print("Get all elements in the list from starting to index 2", names[:2])
print("All elements", names[:2], names[2:])
print("All elements", names[:])

# copying list
# You must be aware, however, that all of these techniques perform a shallow copy. That is, they create a new list containing the same object references as the source list, but don't copy the referred to objects.
names1 = names[:]
print("names1 is names", names1 is names)
print("names1 == names", names1 == names)

names1 = names.copy()
print("names1 is names", names1 is names)
print("names1 == names", names1 == names)

names1 = list(names)
print("names1 is names", names1 is names)
print("names1 == names", names1 == names)

print("Shallow copy demo")
a = [[1, 2], [2, 3]]
acopy = list(a)  # Note shallow copy
acopy[0][0] = 5
print(a[0])
print(acopy[0])
acopy[0] = [-1, -1]  # This is not a problem. We are changing whole element
print(a[0])
print(acopy[0])

# List repetition
l = [1, 2]
print("Repetition: ", l * 3)

print("list with 9 zero elements: ", [0] * 9)

# Note repetition is shallow
l = [0, 1]
new_l = l * 5
print("new_l", new_l)
l.append(-1)
print("new_l", new_l)
print(l)

# finding elements in list
names = ["dora", "spider man ", "papa smurf", "captain america", "mario"]
print("find dora", names.index("dora"))

# count the occurance of elements in the list
print("number of  doras in list", names.count("dora"))

# Find membership
print("Membership", "mario" in ["dora", "spider man ", "papa smurf", "captain america", "mario"])

# Remove element in list
del names[4]
print("Removed mario from the list" , names)
# Remove element by value
names.remove("dora")
print("Removed dora from the list" , names)

x = [1, 2, 3]
x.insert(0, 0)
print("inserted element at 0 in the list", x)
# Converting list to string
print("Convert list to string: ", "|".join(names))
 
# concatenation
x = [1, 2, 3]
y = [4, 5]
print("concatenation creates new lists", x + y)
x += [4, 5]
print("In-place extension", x)
x.extend([6])  # Modifies existing list
print("Extending list", x)

# reverse an element in the list
x = [1, 2, 3, 4]
x.reverse()
print("Reverse elements in the list", x) 
x = [2, 1, 4, 3]
x.sort()
print("Sorted list", x)

# sorted function
x = [2,1,4,3]
y = sorted(x)
print("x: ", x, "y: ", y)
