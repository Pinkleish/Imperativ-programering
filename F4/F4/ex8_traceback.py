# We can use our own functions from others

def is_odd(x):
    a_mistake # This is a mistake
    return x % 2 == 1

def print_is_odd(limit):
    count = 0
    while count < limit:
        if is_odd(count):
            print(str(count) + " is odd.")
        else:
            print(str(count) + " is even.")
        count = count + 1

print(print_is_odd(10))

# When an error occurs in a program, it terminates (exits)
# We see a traceback (also called a stack trace),
# Which shows us the call stack at the time of the error.