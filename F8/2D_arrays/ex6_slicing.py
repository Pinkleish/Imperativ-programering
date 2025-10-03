# In Python, we can 'slice' a list to create a smaller
# list containing only part of it:

arr = ['a','b','c','d','e']

my_slice1 = arr[1:2]
print(my_slice1)
my_slice2 = arr[1:3]
print(my_slice2)
# Are the start and end indices *inclusive* or *exclusive*?

# We can omit the start or the end
print(arr[2:])
print(arr[:3])

# this just gives us a copy:
print(arr[:])

print()
# See Chapter 9: List Slices