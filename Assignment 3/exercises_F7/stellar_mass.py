# This file is used in exercises_F7.py in an optional exercise.
# Do not modify this file!

# Gamma Cassiopeiae, HD 5408, and other stars form a system
# (see: https://en.wikipedia.org/wiki/Star_system).
# That system possibly contains 8 stars, (pg 23. https://iopscience.iop.org/article/10.3847/1538-4365/ac23cb/pdf),
# making it an 'octuple' system.

# The data shows the masses of the stars, measured in solar mass units (M☉),
# shown in python's scientific notation (The mass of our sun is 1M☉.)
# The data is organized into a hierarchy, representing their orbits.

# For our purposes it represents a binary tree. Nodes are either:
# - a leaf: the mass of a star (a floating point number), or
# - an internal node: with *two* child nodes (making it a *binary* tree).

gamma_cas_octuple = (
    # Left subtree: Gamma Cassiopeiae system
    (
        1.7e1,    # Gamma Cas Aa ~17.0 M☉
        (
            9.3e-1,   # Companion Ab ~0.93 M☉
            (
                1.0e0,  # Companion B ~1.0 M☉
                7.0e-1  # Companion C ~0.70 M☉
            )
        )
    ),
    # Right subtree: HD 5408 quadruple (illustrative values)
    (
        5.0e0,       # Star1 ~5.0 M☉
        (
            4.5e0,   # Star2 ~4.5 M☉
            (
                3.5e0,  # Star3 ~3.5 M☉
                2.5e0   # Star4 ~2.5 M☉
            )
        )
    )
)

# This function can be useful for distinguishing internal nodes from leaves:
def is_tuple(node):
    return type(node) is tuple