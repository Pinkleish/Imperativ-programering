# Not for the exam!

print("Reading some lines of text from the file:")

# 'r' means 'text reading mode'
# In this example, the file object allows us to read from the text file.
# We get an error if the file does not exist.
with open('filename.txt', 'r') as file:
    # We can read a single line like this:
    # (this is similar to input())

    line = file.readline()

    line = line.strip() # remove the \n from the end

    print()
    # Note: line includes the newline character- \n

    # the end of file is represented by the empty string: ''
    # ..then we know to stop reading


# These examples show reading/writing text files (as we did previously).
# It is possible to read/write files as binary, but we don't study this in the course.

# File IO is off-syllabus, and not a focus for this course.
# These examples can be adapted for use in the project.