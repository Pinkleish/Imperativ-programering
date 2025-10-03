# Nested for loops are useful for 2D arrays:

my_arr = [[4,5,7],
          [7,3,5],
          [8,2,6]]


# We can use the for loop directly to get the elements:
for row2 in my_arr:
    print(row2) # in this case they are the 'rows'

print()

# We can use nested for loops to iterate through all elements.
# Sum the elements in the array:
sum = 0
for row in range(3):
    print ("row = " + str(row))

    for col in range(3):
        print ("  col = " + str(col) + " and row = " + str(row))
        sum = sum + my_arr[row][col]

print()
print(sum)

