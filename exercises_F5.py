# These exercises relate to Föreläsning 5 - Lists, For Loops, Sorting


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

# use the len function to compute the length of the array, and print it:

# use the len(..) to get the last element of the via its index array, and print it:

exit()
print('==== Q2. ====')
ankor = ducks

# We practice modifying arrays.

# replace 'Farbror Joakim' with 'Magica de Spell' in ducks:

# swap the strings with indices 1 and 2:

# Print the array ducks to check your result:

# Now, print the array ankor:

# Have your changes to ducks affected ankor? (yes/no)
# Write 1-2 sentences to explain.

exit()
print('==== Q3. ====')

array_of_confusion = ["I","am","not","confused"]

def confused(arr):
    for i in range(len(arr)):
        arr[i] = "confused"

confused(array_of_confusion)

print(array_of_confusion)

# Read the code for the function confused(..)
# Think: What values do you expect to see when the array is printed after the function has been invoked?
# Run the code, then explain what you notice. Write 1-3 sentences explaining what you see.
#

# Tips: suggested reading for Lecture 5, Chapter 9.

exit()
print('==== Q4. ====')

# Assign an array containing the numbers of a standard six-sided dice (using integer literals) to a variable called dice
# dice =
# print(dice)

# We use this as our dice for the remaining questions.

exit()
print('==== Q5. ====')

# sum the values in the dice array, using a for loop, with the range(..) function.
# range(..) is a built in function. https://docs.python.org/3/library/stdtypes.html#typesseq-range
# Print the result.

# Having tested your code, convert it into a function which takes an array as an argument.
# Invoke that function on the original dice array and print the result.

exit()
print('==== Q6. ====')

# What happens if we pass a result from the function range(..) as the argument to the built-in function list(..)?
# Experiment in the interactive interpreter. Try passing 1, 2, and 3 integer arguments to the range(..) function.

# Complete the function definition below to return a dice array for a dice with arbitrary number of sides.
# Note that the first element should be 1.

# def create_dice_array(sides):

# Use the function to assign this variable:
# dice_ten_sides =

# Print the value to check.

exit()
print('==== Q7. ====')
# Now we practice calling functions within functions and loops.

# Define a function is_even, to computer whether an integer is even.
# Define another function, which sums the sides of a dice-array, but only sum the sides which are even.

exit()
print('==== Q8. ====')

# Define a function which "rolls" the dice -- i.e. returns one of its elements at random, with equal probability.
# (Hint: adapt the 'guessing' code from the F3 script).

# Use a for loop to roll the dice 10 times, printing out the result each time, to verify it is working correctly.

exit()
print('==== Q9. ====')

# Now we want to count the occurrences of rolls, i.e. how many times a 1 was rolled, how many times a 2 was rolled, etc.
# In Python, we can create an array of zero's like this: [0] * 5
# Create an array of zeros with a length equal to the number of sides of the 'dice' variable. Use an expression for this length.
# Use a for loop to roll the dice 10 times, this time incrementing the element of the count array.
# For example, if we roll a 3, we increment the third element of the array. (Think: which index is this?)

# Use this variable.
# roll_counts =

exit()
print('==== Q10. ====')

# Now we try to visualize the results.
# Write a function containing a for loop to compute the maximum value in an array.
# Create a new array of integers based on the counts, scaling all the values linearly so that the maximum becomes 40.

# i.e. if the max count is 100, all counts are scaled by a factor of 0.4

# Store it in the variable scaled_results:
# scaled_results =

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