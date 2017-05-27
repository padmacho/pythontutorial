student = ("dora", 10, 110.5)  # Student tuple with name, age, height
print("student", student)
print("name", student[0], "age", student[1], "height", student[2])  # access elements in the tuple
print("Number of elements in the tuple", len(student))
# Iterate thru items tuple
for item in student: 
    print(item)
# concatenate tuple
student = student + (30, 25)  # add weight and bmi
print("student", student)
# Repetition with * operator
print("students", student * 2)

# Nested tuple 
rectangle = ((10, 0), (10, 5), (15, 0), (15, 20))
print("Rectangle represented on coordinate plane", rectangle)

# Use index operator to get inner elements in the tuple
print("Co-Ordinate", rectangle[0])
print("Access element inside the Co-Ordinate", rectangle[0][0])

# Single element tuple
student = ("dora",)
print("Single element tuple", student)

# Empty tuple
student = ()
print("Empty tuple", student)

# Parentheses is optional
student = "dora", 10, 110.5  # Student tuple with name, age, height
print("student", student)

# Return tuples
def min_max(items):
    return min(items), max(items)
print("Mix max of the elements in list", min_max([1, 2, 3, 4, 5]))

# Tuple unpacking
# Tuple unpacking is a destructuring operation, which allows us to unpack data structures into named references.
low, high = min_max([1, 2, 3, 4, 5])
print("low", low, "high", high)

print("Simple swapping")
a, b = "hello", "world"
print(a, b)
# swapping
a, b = b, a
print(a, b)

# Constructing tuple from a list
student = tuple(["dora", 10, 110.5])
print("student tuple from list", student)

# Constructing tuple from a string
student = tuple("dora")
print("student tuple from string", student)

# Membership testing
print("5 in (1,2,3,4,5)", 5 in (1, 2, 3, 4, 5))
print("5 not in (1,2,3,4,5)", 5 not in (1, 2, 3, 4, 5))

