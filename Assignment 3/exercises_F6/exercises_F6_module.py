def sort_array_ascending(arr):
    n = len(arr)

    for i in range(n):
        index_of_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[index_of_min]:
                index_of_min = j

        temp = arr[i]
        arr[i] = arr[index_of_min]
        arr[index_of_min] = temp

def sort_array_descending(arr):
    n = len(arr)

    for i in range(n):
        index_of_max = i
        for j in range(i + 1, n):
            if arr[j] > arr[index_of_max]:
                index_of_max = j

        temp = arr[i]
        arr[i] = arr[index_of_max]
        arr[index_of_max] = temp