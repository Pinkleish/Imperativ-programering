# Recall the while loop:

counter = 0
while counter < 10:
    print(counter)
    counter = counter + 1

# Instead we can use the for..in (for loop),
# with a range:
for counter in range(10):
    print(counter)

# This is more compact, and used for cases
# where the number of iterations is fixed.