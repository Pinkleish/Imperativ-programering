# Off the syllabus... just for fun...

import cv2 # opencv-python.
# install with
# mac:
# python3 -m pip --install opencv-python
# windows:
# python -m pip --install opencv-python

img = cv2.imread("mau_210_210.png")
# img is a 3D array!

# it's a numpy array (not a standard python list-of-lists)!
# it is always 'rectangular'.

# so we can for example get the shape directly...
print(img.shape)   # (height, width, 3)
# 3 = Blue,Green,Red

height = 210
width = 210

# Triple-nested for loop - 3D array.
for x in range(width):
    for y in range(height):
        for color in range(2):
            # 'invert' the color channel value:
            img[x][y][color] = 255 - img[x][y][color]

cv2.imwrite('mau_210_210_modified.png', img)

for x in range(width):
    for y in range(height):
        if img[x][y][0] > 0:
            # How does these expressions create the pattern?
            img[x][y][0] = 255 * ((x//4 + y//4) % 2) # blue
            img[x][y][1] = 255 * ((x//4 + y//4) % 2) # gren
            img[x][y][2] = 255 # red
        else:
            # make the pixel white... (not red as I demoed in the lecture)
            img[x][y][0] = 255
            img[x][y][1] = 255
            img[x][y][2] = 255

cv2.imwrite('mau_210_210_modified2.png', img)

# TODO: modify the image in some other way, e.g.
# make a circular pattern
# or concentric circles, or whatever!

print()