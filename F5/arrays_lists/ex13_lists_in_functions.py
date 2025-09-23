kallax1 = ['penna',
           'Think Python',
           'bärbar dator',
           'anteckningsblock']

def my_func(k):
    k[0] = 'hej'
    # There is no return here!

my_func(kallax1)

print(kallax1) # What do we expect to see?

# Modifying arrays in functions is generally
# bad idea.