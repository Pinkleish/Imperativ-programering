
import math
import matplotlib.pyplot as plt

xx = []
yy = []

for x in range(0, 100):
    xx.append(math.pi*2*x/100)

for x in xx:
    yy.append(math.sin(x))

# markers: red, circles, with a regular line between:
plt.plot(xx, yy, 'ro-')

plt.title("plot of y=sin(x)")

plt.xlabel("x")
plt.ylabel("y")


plt.show() # opens the interactive plot viewer...
#plt.savefig('sin_function.png')

plt.clf() # clear the plot to add another.
