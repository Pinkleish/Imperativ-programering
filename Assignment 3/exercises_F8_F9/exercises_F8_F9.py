import naive_bayes
# These are the exercises related to F8 and F9.
# (Start with exercises_F8.py before this one)

# In this exercise we train a simple classifier to distinguish
# between two classes: Stars and Galaxies, based features which we
# can observe from earth. No previous knowledge of Machine Learning is required,
# we simply invoke methods from the module as instructed.
# (No knowledge of machine learning is required for the exam,
# it is just to build basic familiarity with ML concepts.)

# Do not use any other libraries/packages for this question.

# For this exercise, we use a simplified dataset, stars_and_galaxies.csv
# It contains information about known stars and galaxies.
# It contains 4 columns, the first three are features:
# - Infrared - whether the object emits infrared light.
# - UV - whether the object emits ultraviolet light.
# - Variability - whether the brightness varies.
# The final column, Class, is the type of object.
# (open the file in IntelliJ and look at it!)

# We will train a simple classifier based on this dataset,
# and then use it to classify an 'unknown' as either a galaxy or a star,
# based on its feature values (IR, UV and Variability).

# Proceed as follows:
# 1. Run the script so that STDIN is redirected to read from the dataset.
# (Do not redirect STDOUT, so that that print(..) works as normal).

# 2. Read the first line of the dataset, using input(..), and ignore the result.
line = input()
print(f"{line}")
# 3. Read the second line of the dataset, using input(..), assign it to a variable first_line
first_line = input()
print(f"{first_line}")
# 4. Use this code to invoke the split() method on first_line, and store the result.
headers = first_line.split(',')
# What is the type of the variable headers?
#List


# 5. Write a function which evaluates whether a line contains the string 'END', returning
# a boolean.
def contains_END(x):
    split_word = x.split("END")
    return len(split_word) > 1

# 6. use a while loop to read the remaining lines from STDIN using input(..).
# break (exit) the while loop when you encounter a line containing the string 'END' (using the function you defined).
# Hint: if it makes it easier, use the break statement. (look up 'break' in the index of the textbook)
# Include some code to count and print the number of lines.

#For Q7 Initialize empty lists for the features and classes.
features = []
classes = []

#For Q8
def convert(split_line):
    if "Star" in split_line:
        split_line[3] = 0
        classes.append(split_line[3])
    else:
        split_line[3] = 1
        classes.append(split_line[3])

text_line =0
while True:
    line = input()
    if contains_END(line):
        break
    else:
        split_line = line.split(",")
        convert(split_line)
        split_line = split_line[0:3]

        for i in range(len(split_line)):
            if split_line[i] == "0":
                split_line[i] = 0
            else:
                split_line[i] = 1

        features.append(split_line)
    text_line += 1
    print(f"{line:<15} Line {text_line}")
    #print(line + ("    Line: " + (str(text_line))))'

print(f"Features is a 2d array with a length of {len(features)}")
print(f"Classes is an array with a length of {len(classes)}")


# 7. Modify the code in your while loop so that each line of values from the file:
# a. The 'split' method is invoked to separate the values (same as for the header row).
# b. Slice the resulting list, to get the first 3 elements only. These are the features.
# c. Append this list (of length three), as an element, to the list named features.
# features is now a 'list of lists'.
#print(f"{features}")
# 8a. Write a function which converts the class string ('star' or 'galaxy') into an integer 0 or 1.
# Stars are 0, galaxies are 1.
# b. Use this function from inside your while loop to
# append an integer to the list named classes, for each row in the table.
#Function at line 60


# 9. Verify that the list named feature and the list named classes both have length 40.
# If they do not, fix the mistake in your code.

# 10. When using this kind of classifier, it is good if the dataset is 'balanced' -
# i.e. that there are equal numbers of training cases from both classes.
# a. Count the total number of stars in the training dataset, and print the result.
# b. Count the total number of galaxies, and print the result.
# (Use a for loop).
# Use an if statement to check whether the training set is "balanced", and print a message.
# (If you have implemented it correctly, the dataset should be balanced)
stars_number = 0
galaxies_number = 0
for i in classes:
    if i == 0:
        stars_number += 1
    else:
        galaxies_number += 1
print(f"The number of stars is = {stars_number}")
print(f"The number of galaxies is = {galaxies_number}")

# 11. To practice using nested for loops, use nested for loops to count the number
# of values 1 in the list-of-lists named features. Print the result.
number_of_one = 0
for i in range(len(features)):
    for j in range(len(features[i])):
        if features[i][j] == 1:
            number_of_one += 1
print(f"The amount of 1's in features is: {number_of_one}")

# 12. Now we train our classifier. Import the module naive_bayes
# Invoke the function named train(..) with the correct arguments.
# (The first argument should be a list of lists, and the second argument a list of classes)
# If you get an error message when you run the function, read it, and fix your code.
# Store the result of this function call as a variable, it represents our trained model.
trained_model = naive_bayes.train(features,classes)

# 13. Write a function which converts the class (as an integer), back into the string "star" or "galaxy".
def convert_back(clazz):
    if clazz == 1:
        clazz = "Galaxy"
    else:
        clazz = "Star"
    return clazz
# 14. Invoke the classify(..) function from the module, separately, on these two feature-lists:

features_test1 = [0, 0, 1] # Star
features_test2 = [1, 1, 1] # Galaxy
prediction_1 = convert_back((naive_bayes.classify(trained_model,features_test1)))
prediction_2 = convert_back((naive_bayes.classify(trained_model,features_test2)))
print(f"Test1 is predicted to be a {prediction_1} and Test2 is a {prediction_2}")

# You will need to pass the model and the features as arguments.
# (Check the module to check which way round the arguments go.)
# The result in each case will be 0 or 1 representing the predicted class.
# Convert the class number back into a string, and print it in both cases.
# Look at the results - were the model predictions correct? (e.g. features_test1)
# (It is OK if the predictions are wrong)
# Prediction looks to be incorrect.

# 15. Go back and review all the print statements in this script, change them to use f-strings,
# And ensure a more descriptive text is printed, for example, for Q9, the output could look like this (without quotes):
# "There are a total of X galaxies, and Y stars in the dataset."



# (Note: CSV stands for 'comma separated values'. It is a simple, widely used data format.
# CSV format has been adapted for the purposes of this assignment.)
