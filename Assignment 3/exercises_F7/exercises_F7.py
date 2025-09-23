# These are the exercises related to F7.

# Q1. The planets variable represents the masses of planets,
# relative to the mass of earth.
planets = [
    ('mercury', 0.06), ('venus', 0.82), ('earth', 1), ('mars', 0.11)
]


# a. Is 'planets' an array or a tuple?
# b. What is the length of the 'planets'?
# c. What is the type of elements in 'planets'?
# d. What type of elements (and how many) are contained within each element?
# Hint: if you are unsure of the answers, use the type(..) and len(..) functions to help you.

# e. Modify the expression above to include the masses of at least two additional planets:
# https://www.rmg.co.uk/stories/space-astronomy/solar-system-data

# f. Write a function with a planet_name parameter, which returns the mass
# of the specified planet. Use a linear search.
# Hint: See: ex2_using_tuples.py from F7.
# Test your function with some choices of planet, printing the results.


# Q2. Tuples and lists use different kinds of brackets for initialization.
# Give one other important difference between a list and
# a tuple in python. Write 1-3 sentences:
#
#


# Q3. Consider this series sum:
# 1/1 + 1/4 + 1/9 + 1/16 + ... + 1/k²

# a. Write a recursive function which returns the sum
# of the first k terms in the series shown above.
# The function must be recursive (no loops).
# (Hint: it might be helpful to first the function with a for loop)
# (Hint: See: ex5_sum_of_inf_series.py from F7)

# b. Choose a value of k and evaluate your function (for k = 900).
# Multiply the result by 6 take the square root, and print the result:

# c. (Optional) Do you recognize what value the sequence converges to?
# (It is widely used, for example, in calculations relating to orbits.)
#
#


# Q4. **This question is optional/off syllabus, and more challenging!**

# The module stellar_mass.py contains mass information about the masses of stars.

# Import the module into this script, use it to...

# a. Write a Python expression to read the value of 'Star3'.
# b. Write and evaluate, a recursive function to *count the number of* stars.
# c. Write and evaluate, a recursive function to compute the *total mass* of all stars.
#    of the tree.

# Hint:
# def ??(node):
#    if is_tuple(node):
#        l, r  = ??, ??
#        ??
#    else:
#        ??

# d. Can you re-write your answers to b. and c. more concisely using 'conditional expressions'?
# See: Think Python, 18.4. Conditional expressions