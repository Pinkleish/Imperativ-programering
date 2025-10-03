# Compute the sum of the numbers 1..n
n = 10

# Approach 1 - for loop:

def sum_up_to_n_iterative(n):
    sum = 0
    for i in range(n+1):
        sum = sum + 1
    return sum

print(sum_up_to_n_iterative(n))

# Approach 2 - recursive function:

def sum_up_to_n_recursive(n):
    if n == 1:
        result = n
    else:
        result = n + sum_up_to_n_recursive(n - 1)
    return result

print(sum_up_to_n_iterative(n))

# This seems strange and complicated -- but it is
# a powerful concept!