def dungeon_size_input():
    print(f"Select a height:")
    height_raw = int(input())
    while height_raw < 5:
        print(f"Selected height too small")
        height_raw = int(input())
    height_local = height_raw
    print(f"Height has been set to {height_local}")

    print(f"Select a length:")
    length_raw = int(input())
    while length_raw < 5:
        print(f"Selected length is too small")
        length_raw = int(input())
    length_local = length_raw
    print(f"Length has been set to {length_local}")
    return height_local, length_local
height, length = dungeon_size_input()

dungeon_map = []
def dungeon_size(array):
    for i in range(height):
        array.append([])
        for j in range(length):
            array[i].append([])

dungeon_size(dungeon_map)

def dungeon_filled(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = "#"
dungeon_filled(dungeon_map)

def dungeon_frame(array):
    for i in range(1,height-1):
        for j in range(1,length-1):
                array[i][j] = " "
    for row in array:
        print("".join(row))
dungeon_frame(dungeon_map)