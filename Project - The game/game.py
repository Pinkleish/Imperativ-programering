import random
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

dungeon_frame(dungeon_map)

def dungeon_entrance(array):
    #1. Select a random point on the map
    #while both are = 0 select new points
    #if nor the x or y is on the frame:
    #randomly pick an axis at set it to 0
    #set that coordinate to = " "
    height_random = random.randint(0,height-1)
    length_random = random.randint(0,length-1)
    while height_random == 0 and length_random == 0:
        height_random = random.randint(0,height-1)
        length_random = random.randint(0,length-1)
    if 0 < height_random < height-1 and 0 < length_random < length-1:
        coinflip = random.randint(1,2)
        if coinflip % 2 == 0:
            length_random = 0
        else:
            height_random = 0
    array[height_random][length_random] = " "




dungeon_entrance(dungeon_map)

#Prints the map
for row in dungeon_map:
    print("".join(row))