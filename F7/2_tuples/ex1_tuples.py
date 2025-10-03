# Tuples are simply *immutable* lists.

# They are initialized with round brackets....
my_tuple1 = ('a', 'b', 'c')

# of any type:
my_list1 = [True, False, True]
my_tuple2 = (True, False, True)

# ...but a single value needs a comma!
my_tuple3 = (45,)

# ...otherwise it is just a value
just_a_number = (45)

# And elements can be read like arrays:

print("First element is: " + str(my_tuple2[0]))

# However, they are immutable, and cannot be modified:

# This gives an error:
my_tuple4 = (12.3, 45.6, 78.9)
my_tuple4[1] = 0.0