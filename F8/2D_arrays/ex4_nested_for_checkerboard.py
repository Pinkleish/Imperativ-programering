# Nested for loops are useful for 2D arrays:

# How can I make the array look like a checkboard
# (like a schackbräde), 4x4, with 1's and 0's?

my_arr = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

for row in range(4):
    for col in range(4):
        my_arr[row][col] = (row + col) % 2


print(my_arr)