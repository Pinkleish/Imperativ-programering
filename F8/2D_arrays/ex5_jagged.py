# 'Jagged' (sv:Ojämna) array

jagged_array = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9],
    [10]
]

print(jagged_array)


for row in range(len(jagged_array)):
    row_of_array = jagged_array[row]
    for col in range(len(row_of_array)):
        print(jagged_array[row][col])