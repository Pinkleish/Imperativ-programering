# These exercises relate to Föreläsning 5 - Lists, For Loops, Sorting
import random

print('==== Q1. ====')
# This code creates an array from string literals:
ducks = [
    "Kalle Anka",
    "Knatte",
    "Fnatte",
    "Tjatte",
    "Farbror Joakim",
    "Kajsa Anka",
    "Farmor Anka"
]
print(ducks)

# We practice reading values from the array:

# get the first element from the array (Kalle), and print it:
print(ducks[0])
# use the len function to compute the length of the array, and print it:
print(len(ducks))
# use the len(..) to get the last element of the via its index array, and print it:
print(len(ducks[6]))
#exit()
print('==== Q2. ====')
ankor = ducks

# We practice modifying arrays.

# replace 'Farbror Joakim' with 'Magica de Spell' in ducks:
ducks[4] = "Magica de Spell"
# swap the strings with indices 1 and 2:
place_holder = ducks[1]
ducks[1] = ducks[2]
ducks[2] = place_holder

# Print the array ducks to check your result:
print(ducks)
# Now, print the array ankor:
print(ankor)
# Have your changes to ducks affected ankor? (yes/no)
#yes
# Write 1-2 sentences to explain.
#The array is a mutable object with multiple references, ducks & ankor. They both refer to the same object and are
#interlinked in that way, if a change is done to the object then both ducks & ankor reference that changed object.
#exit()
print('==== Q3. ====')

array_of_confusion = ["I","am","not","confused"]

def confused(arr):
    for i in range(len(arr)):
        arr[i] = "confused"

confused(array_of_confusion)

print(array_of_confusion)

# Read the code for the function confused(..)
# Think: What values do you expect to see when the array is printed after the function has been invoked?
#I expect all indices to be set to "confused" and printed
# Run the code, then explain what you notice. Write 1-3 sentences explaining what you see.
#The array has indices 0 through 3 and our function redefines index i to "confused". i is in the range of 3 since
#len(arr) == 3. We then run this function on our array which goes through 0 to 3 and redefines each index as "confused"

# Tips: suggested reading for Lecture 5, Chapter 9.

#exit()
print('==== Q4. ====')

# Assign an array containing the numbers of a standard six-sided dice (using integer literals) to a variable called dice
dice = [1, 2, 3, 4, 5, 6]
print(dice)

# We use this as our dice for the remaining questions.

#exit()
print('==== Q5. ====')

# sum the values in the dice array, using a for loop, with the range(..) function.
# range(..) is a built in function. https://docs.python.org/3/library/stdtypes.html#typesseqarray_of_confusion = ["I","am","not","confused"]
#print the result
def dice_addition(array):
    dice_sum = 0
    for i in range(len(array)):
        dice_sum = dice_sum + dice[i]
        print(dice_sum)

dice_addition(dice)
# ***I didn't realise sum was a command in python until later in this assignment.***

# Having tested your code, convert it into a function which takes an array as an argument.
# Invoke that function on the original dice array and print the result.


#exit()
print('==== Q6. ====')

# What happens if we pass a result from the function range(..) as the argument to the built-in function list(..)?
#or j in range(4,11,2):
    #rint(j)
# Experiment in the interactive interpreter. Try passing 1, 2, and 3 integer arguments to the range(..) function.

# Complete the function definition below to return a dice array for a dice with arbitrary number of sides.
# Note that the first element should be 1.

def create_dice_array(sides):
    dice_array = []
    for number in range(1, sides + 1):
        dice_array = dice_array + [number]
    return dice_array


# Use the function to assign this variable:
dice_ten_sides = create_dice_array(10)
print(dice_ten_sides)

# Print the value to check.

#exit()
print('==== Q7. ====')
# Now we practice calling functions within functions and loops.

# Define a function is_even, to computer whether an integer is even.
def is_even(integer):
    if integer % 2 == 0:
        print(str(integer) + " is even")
    else:
        print(str(integer) + " is odd")
is_even(5)
# Define another function, which sums the sides of a dice-array, but only sum the sides which are even.
def sum_all_even(sides):
    dice_array = create_dice_array(sides)
    tot = 0
    for side in dice_array:
        if side % 2 == 0:
            tot = tot + side
    return tot

print(sum_all_even(6))
#exit()
print('==== Q8. ====')

# Define a function which "rolls" the dice -- i.e. returns one of its elements at random, with equal probability.
# (Hint: adapt the 'guessing' code from the F3 script).

# Use a for loop to roll the dice 10 times, printing out the result each time, to verify it is working correctly.
def dice_roll(sides):
    dice_array = create_dice_array(sides)
    for x in range(1,11):
        roll = random.randint(1, len(dice_array))
        print(roll)

dice_roll(6)

#exit()
print('==== Q9. ====')

# Now we want to count the occurrences of rolls, i.e. how many times a 1 was rolled, how many times a 2 was rolled, etc.
# In Python, we can create an array of zero's like this: [0] * 5
# Create an array of zeros with a length equal to the number of sides of the 'dice' variable. Use an expression for this length.
zero_array = [0] * len(dice)
print(zero_array)
# Use a for loop to roll the dice 10 times, this time incrementing the element of the count array.
# For example, if we roll a 3, we increment the third element of the array. (Think: which index is this?)
for x in range(1,11):
    roll = random.randint(1,6)
    zero_array[roll-1] += 1
print(zero_array)

# Use this variable.
roll_counts = sum(zero_array)
print(roll_counts)
#exit()
print('==== Q10. ====')

# Now we try to visualize the results.
# Write a function containing a for loop to compute the maximum value in an array.
maximum = 0
for number in zero_array:
    if number > maximum:
        maximum = number
print(maximum)
# Create a new array of integers based on the counts, scaling all the values linearly so that the maximum becomes 40.
scaled_results = []
proportions = 40/maximum
for number in zero_array:
    scaled_results = scaled_results + [number*proportions]
print(scaled_results)

# i.e. if the max count is 100, all counts are scaled by a factor of 0.4
# Store it in the variable scaled_results:

# Invoke this function to visualize the results:
def visualize_counts(viz_dice_faces, viz_roll_counts, viz_scaled_counts):
    print(f"{'face':>4} {'count':>8}")
    for i, face in enumerate(viz_dice_faces):
        viz_roll_count = viz_roll_counts[i]
        viz_scaled_count = viz_scaled_counts[i]
        print(f"{face:>4} {viz_roll_count:>8} {'*' * viz_scaled_count}")
exit()
print('==== Q11. ====')

# Now repeat the experiment from the previous question, but using M dice, each with N sides, so that the maximum score on 
# each roll is N*M. Visualize your results as before.

exit()
print('==== Q12. ====')

# Print the roll_counts from Q11 in ascending order.

print('==== END ====')