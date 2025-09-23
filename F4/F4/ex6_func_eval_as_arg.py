# Consider this example

def half_of(x):
    return x / 2

print(
    half_of(
        half_of(8)
    )
)

# We can use the result of the function as
# an argument to the next function.