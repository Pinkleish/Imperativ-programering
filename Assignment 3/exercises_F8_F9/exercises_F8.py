# Here are some exercises for F8.

# We begin with a short exercise on appending elements to lists:

# 1. In Python, we can add an element to the end of a list, increasing its
# length, using the .append(..) method -- (a method is a function attached to an object).
# (See: Think Python, 9.5, List Methods)

# Consider this list:
nearby_stars = ['Proxima Centauri', 'Alpha Centauri A', 'Alpha Centauri B']

# The element to be added is specified as an argument to the method:
nearby_stars.append("Barnard's Star")

# 1a. Now append the string 'Wolf 359' to the list nearby_stars:
nearby_stars.append("Wolf 359")

# 1b. Print the nearby_stars list to verify the change:
print(nearby_stars)

# 2. We create list of lists in Python, like this:
list_of_lists = [['a', 'b', 'c'], ['e', 'f', 'g'], ['h', 'i', 'j']]
# We can access single elements like this:
print(list_of_lists[1][1])

# 2a. Write a line of code like that above to print the letter 'b':
print(list_of_lists[0][1])
# 2b. Write a line of code like that above to print the letter 'j':
print(list_of_lists[2][2])
# 2c. Change the c to C: (use = )
list_of_lists[0][2] = "C"
# 2d. Is 9 the value of len(list_of_lists)? Why not? Write 1-3 sentences.
#List_of_lists contain 3 lists. Aka it would give the length of 3. However, those lists consist of a total of 9 elements.
# 2e. Write a nested for loop to print all the letters a..j contained in the list_of_lists:
for i in range(len(list_of_lists)):
    for j in range(len(list_of_lists[i])):
        print(list_of_lists[i][j])


