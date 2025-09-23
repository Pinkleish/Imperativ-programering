# These are the exercises related to F6.

# As before, follow the instructions to modify the code,
# it will include changes to various files related to F6.
# As before, text answers are written as comments.

# We begin with the Selection Sort (from F5)

# Q1a. Download and extract the code example from F5,
# Copy the selection sort code from the lecture
# (ex20_selection_sort.py) into the file exercises_F6_module.py
# Run exercises_F6_module.py as a script, to ensure it is
# functioning correctly.

# b. Re-organise that code (you pasted into exercises_F6_module.py) to make
# it into a sorting function, which takes the list as a parameter.
# The function should not return a value. Remove any leftover
# code which is not part of the function.

# c. Now we need to test the sorting function.
# We can import the file as a module like this:
import exercises_F6_module

# d. Initialize an array (of numbers or strings) below:
random_array=[5,2,9,6,7]
# and invoke the function on it:
exercises_F6_module.sort_array_ascending(random_array)


# e. ...and print the list to test your function:
print(random_array)
# Q2. Why is it not necessary for your function to return
# the array? Write 1-2 sentences.
# (Hint: see ex13_lists_in_functions.py from F5/array_lists)
#The array is pre-existing and the function refers to it making multiple aliases for it. As the book puts it
# " If the aliased object is mutable, changes made with one name affect the other. "
#

# Q3. Modify the function so that it sorts in
# descending (fallande) order.
# (Hint: this only requires a small modification to one line of code!)
# Rename your function so you don't get confused!
# Run the code again to test:
exercises_F6_module.sort_array_descending(random_array)
print(random_array)

# Now follow the other instructions in exercises_F6_script_part2.py ...

# Q4. (optional/difficult):
# Modify the sorting function so that it counts the
# number of times the values are compared (with > or <),
# and returns that count. Print the number of comparisons
# some arrays of different lengths.

# Could you predict this number by looking at the code?
# Can you write an expression for the number of
# operations in terms of the array length?
# Represent the array length by 'n' in your expression.
# Write it below:
#
#