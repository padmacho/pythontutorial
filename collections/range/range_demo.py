# Most typically we supply only the stop value
# range from 0 to 5
print("Range of 5:", range(5))

for i in range(5):
    print(i)

print("range specifying start and stop values")
# range specifying start and stop values
for i in range(5, 10):
    print(i)

# construct list from range
print("List from range", list(range(5)))

# Range with step argument
print("Range with step argument", list(range(5, 10, 2)))

print("Summary")
print("stop argument", range(5))
print("start,stop argument", range(5, 10))
print("start,stop,step argument", range(5, 10, 2))
