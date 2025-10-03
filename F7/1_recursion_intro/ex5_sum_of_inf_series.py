# Sum of Infinite Series

# We might want to compute the sum of a series
# which follows a pattern:

# 1/1 + 1/2 + 1/3 + 1/4 + ... + 1/k

# Here the ... represents the (finite) missing terms.

# Suppose we want to compute the sum of the first k terms:
k = 100
# Can we write a function using a for loop?
sum = 0
for i in range(1, k + 1):
    sum = sum + 1/k

# Can we write a recursive function to do this?
def sum_fraction(x):
    if x == 1:
        return 1/1
    else:
        return 1/x + sum_fraction(x - 1)
