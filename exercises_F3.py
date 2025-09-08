import random
# These exercises relate to Föreläsning 3 - Conditionals + While
# We also begin to practice with print(..) and keyboard input.

# In this worksheet, you can use the IDE as a text editor only.
# But practice running the python script directly from the command line.

print('==== Q0. ====')

# Your first task is to show that you can run this script for the command prompt (kommandotolken).
print("This script is being executed in the python interpreter!")

# Write a comment on the line below showing the command you used on your computer to run this script:
# python3 exercises_F3.py

# When you have completed the question above - remove or comment out the line below:
#exit()

print('==== Q1. ====')

PYTHON_VERSION = 3
# When used with two strings, the + operator will concatenate (join) the strings.
# This line of code contains an error, because we try to concatenate a string and an int (which is invalid)
# Modify the line below to include the str(..) function so that two strings are concatenated, to fix the error.
print("This script is intended for Python version: " + str(PYTHON_VERSION))

#exit()

print('==== Q2. ====')
# This code prints the númbers 0..9 in increasing order
count = 5
while count >= 0:
    print(count)
    count = count - 1

# Modify it so instead it starts at 5, counting down to (and including) 0, counting down.

# When you have completed the question above - remove or comment out the line below:
#exit()

print('==== Q3. ====')

# This code prints the numbers 0 to 9.
count = 0
while count < 10:
    if count % 2 == 0 and count % 5 == 0:
            print("CI at Malmö")
    elif count % 2 == 0:
        print("CI")
    elif count % 5 == 0:
        print("Malmö")
    else:
        print(count)
    count = count + 1

# For this question, modify it so that it prints:
# 'CI', instead of the count, if the count is even.
# 'Malmö', instead of the count, if the count is a multiple of 5.
# 'CI at Malmö' instead of the count, if both conditions are true.
# If none of those conditions is true, the count is printed as above.

# When you have completed the question above - remove or comment out the line below:
#exit()

print('==== Q4. ====')
# This question is about nested and chained booleans.

# We have some variables representing the state of a dinosaur:
has_food = False
is_threatened = False
is_sleeping = False

# Write some code which prints one of these 4 strings according to the values of those variables:
# "Eat the food!" - not threatened, and has food. (regardless of whether asleep or not)
if has_food and not is_threatened:
    print("Eat the food!")
# "Roar at the threat!" - if the dinosaur is threatened.
elif is_threatened:
    print("Roar at the threat!")
# "Keep sleeping..." - if the dinosaur is asleep and not threatened.
elif is_sleeping and not is_threatened:
    print("Keep sleeping...")
# "Do nothing." - none of the above.
else:
    print("Do nothing")

# Test your code by changing the variables to different values.
# If you have got it working, can you simplify your code further?

# When you have completed the question above - remove or comment out the line below:
#exit()

print('==== Q5. ====')
# In this question - the computer randomly guesses a number we have chosen.

#It is standard practice to put imports at the top of the file. Move it there!
my_number = 27
iteration = 1
guess = random.randint(1, 50)
print("My number is " + str(my_number))
#print("Computer's guess is " + str(guess))
print(iteration)
while guess != my_number:
    guess = random.randint(1, 50)
    iteration = iteration + 1
    print("Iteration:" + str(iteration))

# Write some additional code so that, the variables my_number and guess are compared, so that...
# "too low!" is printed if the guess is too low.
# "too high!" is printed if the guess is too high.
# A message of your choice printed if the guess is correct.
# Hint: try to write a single, chained if statement.

# When you have done this, modify the code so that the computer keeps randomly guessing in the same range,
# until it gets the answer correct, (when it needs to stop).

# Modify the code to count the number of iterations, and print it.

# When you have completed the question above - remove or comment out the line below:
#exit()

print('==== Q6. ====')

# Copy and paste your solution to Q5.
my_number = 27
low = 1
high = 50
guess = random.randint(1, 50)
while guess != my_number:
    if guess < my_number:
        low = guess
        print("Lower bound is " + str(low))
    elif guess > my_number:
        high = guess
        print("Upper bound is " + str(high))
    guess = random.randint(low, high)
print(":)")

# Now modify the solution so that:
# in addition to printing the message, the range is adjusted with each guess.
# e.g. If the computer guesses 10, and it's too low, 10 becomes the new lower bound.
# Be careful with bounds - are they 'inclusive' or 'exclusive'.

# (It should now take less iterations to guess)

# When you have completed the question above - remove or comment out the line below:
#exit()

print('==== Q7. ====')
# In this question we practice with keyboard input.

a = input("Enter a string:")
print("You entered: " + a)
b = input("Enter another string:")
print("You entered: " + b)
if len(a) == len(b):
    print(a + " " + b)
else:
    print("The longest string is: " + max(a,b))

# Write code to print the longest of the two strings.
# If the strings are equal length, print both of them.

# When you have completed the question above - remove or comment out the line below:
#exit()

print('==== Q8. ====')

# In this question, the user must enter a password. Valid passwords are between 5 and 10 digits.
# Continue to repeatedly prompt the user for a password of password, until they enter one which satisfies the criteria.
password = input("Enter a password (5-10 characters):")
while len(password) > 10 or len(password) < 5:
    print("password not valid")
    password = input("Enter a password (5-10 characters):")
print("password valid")

print('==== END ====')