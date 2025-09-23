
# We can define multiple arguments for our function:

def print_n_times(s, n):
    count = 0
    while count < n:
        print(s)

# This function does not have a return value.

print_n_times("hej",
              10)

# Parameter order matters, this is incorrect:
print_n_times(10, "hej")









