# Each time a function is evaluated,
# a different value is used for the argument:

def is_odd(x):
    return x % 2 == 1


count = 0
while count < 10:
    print(is_odd(count))
    count = count + 1
