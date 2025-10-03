# From "Think Python"

def print_n_times(string, n):
    if n > 0:
        print(string)
        print_n_times(string, n-1)

print_n_times('hej!', 4)

# Draw Stack Diagram!