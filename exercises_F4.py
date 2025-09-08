# These exercises relate to Föreläsning 4 - Defining Functions

print('==== Q1. ====')
# Consider this code:

def is_even(num):
    return num % 2 == 0

print("is_even(5) evaluates to " + str(is_even(5)))
print("is_even(6) evaluates to " + str(is_even(6)))

# What is the name of the function? (write your answer here...)
# How many parameters (parametrar) does it take?
# Which type (datatyp) of value does it return?
# What is the type of arguments are when invoking/calling (anrop) the function?
# How many times is the function evaluated in above?

# Define a new function, is_odd, and print some examples of evaluation as before.

exit()
print('==== Q2. ====')

# Write a function which takes two string arguments and returns the one which is longest.
# If the strings are the same length, concatenate (join, konkatenera) them (with a space (mellanslag) between).
# (Assume the inputs are strings, do not validate this.)
# To test your function, invoke your function for some different string values, and print the results, as in Q1.

exit()
print('==== Q3. ====')

# Implement your own version of the built-in 'abs' function, using an if statement and conditional operators.
# To test your function, invoke your function for some different integer and float values, and print the results.
# Test both positive and negative arguments.

exit()
print('==== Q4. ====')

# Consider this function.

def add(x, y):
    x + y

sum = add(3,4)
print(sum)

# What is the value of the variable sum after assignment in the example above?

# The function is not working as it should. Fix it. Run again to test.

exit()
print('==== Q5. ====')

# Consider this code. Before you run it, write down what you expect the output to be:
# print 1:
# print 2:
# print 3:
# print 4:
# print 5:

# Think: In order do you expect the outputs to occur?

x = "pettson"
print("1: " + x)

def my_func(x):
    print("2: " + x)
    x = "findus"
    print("3: " + x)

print("4: " + x)
my_func("pettson och findus")
print("5: " + x)

# Why are the print statements 1..5 not printed out in the order they occur in the code? Write 1-2 sentences.
# (print 3) and (print 5) do not show the same value, why not? Write 1-2 sentences.

exit()
print('==== Q6. ====')

def product(x, y):
    #print("x = " + str(x) + ", y = " + str(y))
    return x * y

# When we write a complex expression, we can split it over multiple lines to improve readability:
big_product = product(
        product(2,3),
        product(4,5))


# (Think first, then uncomment the print statement to check your answers).
# How many times is the function product(..) evaluated above?
#
# What are the values of 'x' and 'y' in each case?
#
#
#

print('==== END ====')