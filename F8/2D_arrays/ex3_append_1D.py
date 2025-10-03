# Example showing append on a 1D array.

# We can add an element to the end of a list, increasing its
# length, using the .append(..) method -- (a method is a function attached to an object).
# (See: Think Python, 9.5, List Methods)

arr = ['a', 'b', 'c']

# Append 'd' to the array:

arr.append('d')

# now print the array:

print(my_list)

# We often append to an empty list...
my_list = []
for i in range(10):
    my_list.append(i ** 2)
