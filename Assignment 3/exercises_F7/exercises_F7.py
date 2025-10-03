# These are the exercises related to F7.

# Q1. The planets variable represents the masses of planets,
# relative to the mass of earth.
planets = [
    ('mercury', 0.06), ('venus', 0.82), ('earth', 1), ('mars', 0.11), ("jupiter", 317.89), ("uranus", 14.56)
]


# a. Is 'planets' an array or a tuple?
#    an array of tuples
# b. What is the length of the 'planets'?
#    4
# c. What is the type of elements in 'planets'?
#    the array consists of tuples
# d. What type of elements (and how many) are contained within each element?
#    The first tuple contains 1 string & 1 float, the second contains 1 string & 1 float, the 3rd contains 1 string
#    & 1 integer, the 4th contains 1 string & 1 float.
# Hint: if you are unsure of the answers, use the type(..) and len(..) functions to help you.

# e. Modify the expression above to include the masses of at least two additional planets:
# https://www.rmg.co.uk/stories/space-astronomy/solar-system-data

# f. Write a function with a planet_name parameter, which returns the mass
# of the specified planet. Use a linear search.
# Hint: See: ex2_using_tuples.py from F7.
# Test your function with some choices of planet, printing the results.
def linear_search(planet):
    for tuples in planets:
        if (tuples[0] == planet):
            return tuples[1]
print(linear_search("jupiter"))


# Q2. Tuples and lists use different kinds of brackets for initialization.
# Give one other important difference between a list and
# a tuple in python. Write 1-3 sentences:
#A list is mutable meaning it can be altered after the fact. On the other hand a tuple is inmutable, meaning it
# is incapable of being changed when it has been set. In other words tuples are read only.



# Q3. Consider this series sum:
# 1/1 + 1/4 + 1/9 + 1/16 + ... + 1/k²

# a. Write a recursive function which returns the sum
# of the first k terms in the series shown above.
# The function must be recursive (no loops).
# (Hint: it might be helpful to first the function with a for loop)
# (Hint: See: ex5_sum_of_inf_series.py from F7)
def fraction(k):
    if k == 1:
        return 1
    else:
        return 1/k**2 + fraction(k-1)

# b. Choose a value of k and evaluate your function (for k = 900).
# Multiply the result by 6 take the square root, and print the result:
k = 900
print(((fraction(k))*6)**0.5)
# c. (Optional) Do you recognize what value the sequence converges to?
# (It is widely used, for example, in calculations relating to orbits.)
# pi



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