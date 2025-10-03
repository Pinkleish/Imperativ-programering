# We sometimes use tuples to represent small groups of values
# that represent the same "thing".

# We avoid changing the value by accident.

# e.g.
coordinates = (55.60, 13.00)

# For example, we can represent the number
# of items in a shopping cart like this:
my_shopping = [
    ('äpple', 3),
    ('kex', 2),
    ('mjölk', 1),
]

# Can we write a linear search to find how many kex?

def get_shopping_count(thing):
    for my_tuple in my_shopping:
        if (my_tuple[0] == thing):
            return my_tuple[1]

print(get_shopping_count('kex'))