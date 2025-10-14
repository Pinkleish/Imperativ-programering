# We typically assign an alias to the imported module.
import matplotlib.pyplot as plt
# (many of the alias have a convention, e.g. numpy is usually np)

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis((0, 6, 0, 20))
plt.show()

# ro means:
# r - red
# o - circle

# see:
# https://www.w3schools.com/python/matplotlib_markers.asp