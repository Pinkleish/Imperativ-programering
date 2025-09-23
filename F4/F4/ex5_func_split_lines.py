def is_odd(x):
    return x % 2 == 1


# We are allowed to use multiple lines when calling
# a function
print(
    "10 is odd: "
    + str(is_odd(10))
)

# Of course, can mix existing functions with our own.