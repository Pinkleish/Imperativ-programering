# The Fibonacci Sequence

# The sequence begins with 0, 1
# each subsequent term is the sum of the two previous terms:

# 0, 1, 1, 2, 3, 5, 8, ...

# We use the ... to show that it goes on forever.

# Can we write a recursive function to compute the nth term?

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n- 2)

print(fibonacci(7))