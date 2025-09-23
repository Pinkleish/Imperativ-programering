# We can re-assign variables...
x = 5 * 6
y = x
x = x + 1


# The value of the variable can change.
# But the values *themselves* are *immutable*
# We cannot modify the value 6, or "Hej!"

# Lists/Arrays are *mutable*:
y = [4,5,6] # new array, assign variable.
y[0] = 7 # replace an element, array modified.
y = [8,9,10] # re-assign variable
y = 11 # re-assign variable again.