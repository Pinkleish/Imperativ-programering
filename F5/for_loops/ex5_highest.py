# What is the lowest/highest element in the array/list?

arr = [200, 100, 150]

# This is broken! Can you see why?
# What happens if there are high numbers in the array?
# What can we do instead?
lowest = 99999999
index_of_lowest = -1

for i in range(len(arr)):
    x = arr[i]
    if x < lowest:
        lowest = x
        index_of_lowest = i

print(lowest)
print(index_of_lowest)


