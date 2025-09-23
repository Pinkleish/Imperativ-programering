# Write an algorithm to find the index
# of the *element 10* in the list,
# using a for loop.

my_list = [3, 6, 10, 1, 2]

result = "not found"

for i in range(len(my_list)):
    if my_list[i] == 100:
        result = i

print(result)

# This is called a "Linear Search"
