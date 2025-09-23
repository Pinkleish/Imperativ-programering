# The questions for F6 continue here from exercises_F6_script.py

# Read this code...
import sys
import exercises_F6_module

# Read all the lines from STDIN
# (This is equivalent to a while loop with input(..))
lines = list(sys.stdin)

# Make a new array of zeros.
numbers = [0] * len(lines)

# Convert the strings to ints
for i in range(len(lines)):
    numbers[i] = int(lines[i])
exercises_F6_module.sort_array_descending(numbers)
print("TODO - print the numbers in reverse order.")
for i in range(len(numbers)):
    print(numbers[i])
# Q5.
# Before working on this script, we run it:
# Using the terminal/kommandotolken for your operating system, execute the script
# so that STDIN is redirected to read from the file 'numbers.txt',
# (which contains a list of numbers), and STDOUT is redirected to a (new)
# file to be named 'numbers_descending.txt', both in this directory.
# Copy below the line you typed into your terminal:
#python exercises_F6_script_part2.py > numbers_descending.txt < numbers.txt
#

# Q6. This script is supposed to read integers
# from STDIN, and then print them to STDOUT (using print()),
# sorted in descending order, in the same format as the input.
# This functionality is missing/incomplete ("TODO").
# By importing the sorting function your module,
# implement the missing functionality.
# Test the functionality by running this script, and inspecting the file numbers_descending.txt
# (Do not use the built-in sorted(..) function.)


# Optional:
# In addition to running the script from the terminal/kommandotolken, configure
# the run configuration in IntelliJ (or your choice of IDE) so that it achieves the same
# result as the STDIN/OUT redirection.