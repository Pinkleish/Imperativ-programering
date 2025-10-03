import math


def squared(x):
    return x**2

def area_circle(radius):
    return squared(radius) * math.pi

def many_circles():
    for i in range(10):
        # Put a line breakpoint on the line below.
        # Experiment with 'Step Over', 'Step Into', 'Step Out'
        print("Area of circle with radius " + str(i) + " is " + str(area_circle(i)))

many_circles()