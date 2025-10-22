import random
import module
PLAYER_ICON = "P"
TREASURE_ICON = module.TREASURE_ICON
TRAP_ICON = module.TRAP_ICON

def map_array():
    #Opens the txt file as "map"
    with open("dungeon_map.txt","r") as map:
        # Makes a list of the lines in map
        lines = map.readlines()
    # Creates an array
    dungeon_map = []
    # Iterates over the list & removes new lines, makes a list of the stripped lines and appends that list to the array
    for lines in lines:
        line = lines.strip("\n")
        row = list(line)
        dungeon_map.append(row)
    return dungeon_map

dungeon_map = map_array()

def dungeon_dimensions(array):
    height = len(array)
    length = len(array[0])
    return height,length
height,length = dungeon_dimensions(dungeon_map)

def player_start(array):
    # Checks the upper frame for an entrance
    for i in range(len(array[0])):
       if array[0][i] != "#":
           array[0][i] = PLAYER_ICON
           return 0,i

    # Checks lower frame for an entrance
    for j in range(len(array[height-1])):
        if array[height-1][j] != "#":
            array[height-1][j] = PLAYER_ICON
            return height-1,j


    # Checks left column for an entrance
    for y in range(len(array)):
        if array[y][0] != "#":
            array[y][0] = PLAYER_ICON
            return y,0

    # Checks right column for an entrance
    for x in range(len(array)):
        if array[x][length-1] != "#":
            array[x][length-1] = PLAYER_ICON
            return x,length-1
    else:
        return None

player_height, player_length = player_start(dungeon_map)


def map_hide(array):
    # Creates a new list
    players_map = []
    # Copy the rows from the map into the new list, the 'index' [:] ensures it's a new object and not a reference
    for row in array:
        players_map.append(row[:])
    for i in range(len(players_map)):
        for j in range(len(players_map[i])):
            # Nested for loops that looks for treasure or traps & replaces their icon with "?"
            if players_map[i][j] == module.TREASURE_ICON or players_map[i][j] == module.TRAP_ICON:
                players_map[i][j] = "?"
    return players_map

players_map = map_hide(dungeon_map)





def score_treasure_or_trap(array,player_height,player_length):
    # Check whether "?" icon is treasure or trap and returns the value of it
    if array[player_height][player_length] == module.TREASURE_ICON:
        added_score = random.randint(1,5)
        movement_penalty = 0
        print(f"A treasure! +{added_score} score")
    else:
        added_score = -1
        movement_penalty = 1
        print(f"Uhoh, a trap :( {added_score} score & -{movement_penalty} moves")
    return added_score,movement_penalty

def score_calculation(score,new_score):
    if score+new_score < 0:
        score = 0
    else:
        score += new_score
    return score

def input_direction(direction):
    # A dictionary that keeps track of what each valid input represents
   movement = {
       "w": (-1,0),
       "s": (1,0),
       "a": (0,-1),
       "d": (0,1)
   }
   # Matches the direction input against the dictionary & returns it's values
   for i in movement:
        if i == direction:
           player_move_height = movement[i][0]
           player_move_length = movement[i][1]
           return player_move_height, player_move_length


def player_movement_empty(player_array,player_height,player_length,player_move_height,player_move_length):
    player_array[player_height][player_length] = " "
    player_height += player_move_height
    player_length += player_move_length
    player_array[player_height][player_length] = PLAYER_ICON
    for row in player_array:
        print("".join(row))
    return player_height,player_length



# This is a pretty long function & I wanted to divide it up into several smaller functions
# but there were so many local variables that it I found it harder to follow when divided

def player_movement(array,player_array,player_height,player_length):
    # Calculate the moves based on area inside of dungeon
    player_movement_start_amount = int(((height-1) * (length-1))/2)
    entrance = (player_height,player_length)
    # Keep track of moves,score & if player wants to leave
    leaving = False
    moves_taken = 0
    score = 0
    # Prints the map
    for row in player_array:
        print("".join(row))
    # Stop while loop when all moves have been taken
    while moves_taken != player_movement_start_amount:
        # Stops while loop if player want to leave dungeon
        if leaving:
            break
        # Asks for input and makes it lowercase
        print(f"Your score is: {score}")
        print(f"Use wasd to move, you have {player_movement_start_amount-moves_taken} moves left")
        move = input().lower()
        # Checks for valid move and calls input_direction to get the values of the move
        if move in("w","a","s","d"):
            player_move_height, player_move_length = input_direction(move)
            # Checks if player wants to leave
            if player_height+player_move_height == entrance[0] and player_length+player_move_length == entrance[1] and moves_taken > 0:
                leaving = True
            # Checks if player tries to walk into wall
            elif player_array[player_height+player_move_height][player_length+player_move_length] == "#":
                print(f"Can't go there, try again")
            elif player_array[player_height+player_move_height][player_length+player_move_length] == "?":
                # Sets the slot the player is moving away from to empty & sets the new coordinates as the player
                player_height,player_length = player_movement_empty(player_array,player_height,player_length,player_move_height,player_move_length)
                # Checks whether the "?" was a treasure or trap
                new_score,movement_penalty = score_treasure_or_trap(array,player_height,player_length)
                moves_taken += 1+movement_penalty
                score = score_calculation(score,new_score)
            else:
                # Moves the player properly into place
                player_height,player_length = player_movement_empty(player_array,player_height,player_length,player_move_height,player_move_length)
                moves_taken += 1
    # If the player runs out of moves it's game over & score is 0
    if moves_taken == player_movement_start_amount:
        score = 0
        print(f" Game over! You didn't make it out in time, your final score is: {score}")
    # If player leaves it's game over and prints score
    else:
        print(f"Game over! Your final score is: {score}")


player_movement(dungeon_map,players_map,player_height,player_length)

