# The previous examples worked because
# range(..) is an example of a *sequence*

# for..in can be used with any sequence:

print("again, a range:")
for c in range(5):
    print(c)

print("but also, a string:")
for c in 'CD100A':
    print(c)

print("or any kind of array:")
for t in [True, False, True]:
    print(t)

my_arr = ['ole', 'dole', 'doff']
for t in my_arr:
    print(t)