import random
import module
TREASURE_ICON = module.TREASURE_ICON
TRAP_ICON = module.TRAP_ICON

def dungeon_size_input():
    # Asks user to enter a number
    print(f"Select a height:")
    height_raw = int(input())
    # Makes sure that the number isn't too small
    while height_raw < 5:
        print(f"Selected height too small")
        height_raw = int(input())
    # Reaffirms the selected height
    print(f"Height has been set to {height_raw}")

    print(f"Select a length:")
    length_raw = int(input())
    while length_raw < 5:
        print(f"Selected length is too small")
        length_raw = int(input())
    print(f"Length has been set to {length_raw}")
    # Returns the values and then defines global variables as the return of the function once called
    return height_raw, length_raw
height, length = dungeon_size_input()

def dungeon_attributes():
    # Asks user to give 3 numbers for different attributes
    print(f"You now need to select the amount of each attribute for this dungeon")
    print(f"Select amount of treasure:")
    treasure_raw = int(input())
    print(f"Select amount of traps:")
    traps_raw = int(input())
    print(f"Select amount of inner walls:")
    walls_raw = int(input())
    # Makes sure that the sum of the attributes isn't bigger than the area inside of the dungeon walls
    while (treasure_raw + traps_raw + walls_raw) > ((height-2) * (length-2)):
        print(f"The total amount of attributes is larger than the dungeons area, please select again:")
        treasure_raw = int(input())
        traps_raw = int(input())
        walls_raw = int(input())
    print(f"Amount of treasure is set to: {treasure_raw}")
    print(f"Amount of traps is set to: {traps_raw}")
    print(f"Amount of walls is set to: {walls_raw}")
    return treasure_raw, traps_raw, walls_raw
treasure, traps, walls = dungeon_attributes()


dungeon_map = []
def dungeon_size(array):
    # Creates an empty 2d array based on height and length
    for i in range(height):
        array.append([])
        for j in range(length):
            array[i].append([])

dungeon_size(dungeon_map)

def dungeon_filled(array):
    # Fills the empty array with "#"
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = "#"
dungeon_filled(dungeon_map)

def dungeon_frame(array):
    # Fills out everything but the outer walls with " "
    for i in range(1,height-1):
        for j in range(1,length-1):
                array[i][j] = " "

dungeon_frame(dungeon_map)

def dungeon_entrance(array):
    # Select a random point inside of the walls
    height_random = random.randint(0,height-1)
    length_random = random.randint(0,length-1)
    # While both are = 0 select new points, this makes sure it isn't a corner
    while height_random == 0 and length_random == 0:
        height_random = random.randint(0,height-1)
        length_random = random.randint(0,length-1)
     # If no point is on the frame then randomly set either height or length to = 0
    if 0 < height_random < height-1 and 0 < length_random < length-1:
        coinflip = random.randint(1,2)
        if coinflip % 2 == 0:
            length_random = 0
        else:
            height_random = 0
    # Set the resulting coordinate to = " "
    array[height_random][length_random] = " "
    return array[height_random][length_random]

entrance = dungeon_entrance(dungeon_map)

def dungeon_walls_place(array):
    # Randomly places amount of walls selected by user
    walls_placed = 0
    while walls_placed != walls:
        height_random = random.randint(2,height-3)
        length_random = random.randint(2,length-3)
        # Checks the slot isn't occupied
        if array[height_random][length_random] == " ":
            array[height_random][length_random] = "#"
            walls_placed += 1

dungeon_walls_place(dungeon_map)

def dungeon_walls_extend(array):
    for i in range(2,height-3):
        for j in range(2,length-3):
            if array[i][j] == "#":
                # Randomly selects how many times the wall tries to be extended
                extension_random = random.randint(5,10)
                # Randomizes what direction to extend said wall and makes sure only one direction is selected
                while True:
                    height_random = random.randint(-1,1)
                    length_random = random.randint(-1,1)
                    if height_random + length_random == -1 or height_random + length_random == 1:
                        break
                # Extends the wall in the chosen direction by the amount decided by extension_random
                for iteration in range(1,extension_random+1):
                    height_extension = height_random*iteration
                    length_extension = length_random*iteration
                    # Makes sure the wall isn't about to extend outside of the allowed area
                    if 1 < i+height_extension < height-2 and 1 < j+length_extension < length-2:
                        # Places a temporary icon instead of wall to avoid extending extensions
                         array[i+height_extension][j+length_extension] = "T"

dungeon_walls_extend(dungeon_map)

def dungeon_walls_fix(array):
    # Replaces the temporary icon with a wall
    for i in range(2,height-2):
        for j in range(2,length-2):
            if array[i][j] == "T":
                array[i][j] = "#"

dungeon_walls_fix(dungeon_map)



def dungeon_treasure(array):
    # Initiate a counter to keep track of how many treasures have been placed
    treasure_placed = 0
    while treasure_placed != treasure:
        # Pick random coordinate inside of the frame, -2 to make sure that the check always is inside of my array
        height_random = random.randint(1,height-2)
        length_random = random.randint(1,length-2)
        adjacent_empty = 0
        # Check if selected slot is available
        if array[height_random][length_random] == " ":
            # Check if there is already a treasure in any adjacent coordinate 2+ since its an exclusive upper bound
            for i in range(height_random-1,height_random+2):
                for j in range(length_random-1,length_random+2):
                    if array[i][j] != TREASURE_ICON:
                        adjacent_empty += 1
        # If the checked grid is empty then place a treasure
        if adjacent_empty == 9:
            array[height_random][length_random] = TREASURE_ICON
            treasure_placed += 1

dungeon_treasure(dungeon_map)

def dungeon_traps(array):
    # Identical to dungeon_treasure with a few variables changed to place traps instead.
    traps_placed = 0
    while traps_placed != traps:
        height_random = random.randint(1,height-2)
        length_random = random.randint(1,length-2)
        adjacent_empty = 0
        if array[height_random][length_random] == " ":
            for i in range(height_random-1,height_random+2):
                for j in range(length_random-1,length_random+2):
                    if array[i][j] != TRAP_ICON:
                        adjacent_empty += 1
        if adjacent_empty == 9:
            array[height_random][length_random] = TRAP_ICON
            traps_placed += 1

dungeon_traps(dungeon_map)

#Prints the map
#for row in dungeon_map:
    #print("".join(row))

with open("dungeon_map.txt", "w") as map:
    for row in dungeon_map:
        map.write("".join(row) + "\n")