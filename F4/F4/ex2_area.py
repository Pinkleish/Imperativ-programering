# This fits with our existing understanding of a
# mathematical function:

def get_circle_area(radius):
    return 3.14159 * radius ** 2

# Very different from this:
# circle_area = 3.14159 * radius ** 2

def get_circle_perimeter(radius):
    return radius * 2 * 3.14159

print(get_circle_area(3))
print(get_circle_perimeter(3))

