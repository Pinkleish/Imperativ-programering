# This is not for the exam!

# We can also read and write files directly in our python code.
# This requires some additional functions and keywords.

print("Writing some lines of text to the file...")

# open(..) is a built-in function, which returns a 'file object',
# this is assigned to the variable 'file', and holds and object
# representing the file, while it is open.

# which we can use to read and write to the file, depending on the mode.
# 'w' means 'text writing mode' - printing data to the file.

# The 'with' keyword ensures the file is closed properly if there is an error.

# This does not use STDOUT -- and nothing is printed to the console,
# it goes directly to the named file, regardless of any STDOUT redirection.

with open('filename.txt', 'w') as file:
    file.write("banan\n")
    file.write("melon\n")
    file.write("kiwi\n")
    file.write("citron\n")

    # These are similar to print()
    # There is a key difference -- look at the file -- what is it?


# If the file exists, it is overwritten (and the contents is lost!)
# If the file does not exist, it is created.

