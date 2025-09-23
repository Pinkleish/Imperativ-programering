# Selection Sort
arr = [64, 25, 12, 22, 11]
n = len(arr)

for i in range(n):
    # (Indices 0,..,i-1 are sorted already)
    # Find the minimum element from i+1..n-1:
    index_of_min = i
    for j in range(i + 1, n):
        if arr[j] < arr[index_of_min]:
            index_of_min = j
    # ...swap it to the i:th position:
    temp = arr[i]
    arr[i] = arr[index_of_min]
    arr[index_of_min] = temp

print("Sorted array:", arr)