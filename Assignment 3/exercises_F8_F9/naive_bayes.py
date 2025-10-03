# This is a module intended for use in exercises_F8_F9.py

# Do not modify this file!

# You are not expected to understand the contents of the functions,
# but you should look at the names and order of the function parameters, for use
# in the exercise.

import math

# Naive Bayes Binary Classifier
# - The model is a *classifier* - it returns a 'class label' for an input.
# - It is a *binary* classifier it supports only two output classes, 0 and 1.
# - It uses 'Naive Bayes': features are treated as independent binary variables (Bernoulli events).

# NB classifiers are simple, and are widely used for e.g. text classification, where the binary
# feature represents the inclusion of a particular word.

# Train a model for a set of features and classes.
def train(features, classes):
    if len(classes) == 0:
        raise ValueError("You must supply training data.")

    if len(features) != len(classes):
        raise ValueError("The number of feature vectors and classes must match")

    if not all(isinstance(x, int)
               and (x == 1 or x == 0)
               for x in classes):
        raise ValueError("This is *binary* classifier, classes must be 0 or 1.")

    n_features = len(features[0])
    if not all(len(f) == n_features
               for f in features):
        raise ValueError("feature vectors need to be the same length.")

    if not all(
        all(f_i == 1 or f_i == 0
            for f_i
            in f)
        for f in features):
        raise ValueError("features must be binary: 0 or 1 only")

    # Feature counts for each class:
    feature_counts0 = [0] * n_features
    feature_counts1 = [0] * n_features
    # Counts for each class:
    count0 = 0
    count1 = 0
    # Count the features
    for feature_vector, clazz in zip(features, classes):
        if clazz == 0:
            count0 += 1
            for i in range(n_features):
                feature_counts0[i] += feature_vector[i]
        else:
            count1 += 1
            for i in range(n_features):
                feature_counts1[i] += feature_vector[i]

    # Convert counts to probabilities with Laplace smoothing (aka plus one smoothing)
    theta0 = [(c + 1) / (count0 + 2) for c in feature_counts0]
    theta1 = [(c + 1) / (count1 + 2) for c in feature_counts1]

    # Return feature count vectors as the model:
    return theta0, theta1

def classify(model, features):
    if len(model) != 2:
        raise ValueError("Incorrect model.")

    if (len(features) != len(model[0])) or (len(features) != len(model[1])):
        raise ValueError("Incorrect model/features")

    theta0, theta1 = model
    # Compute Log-probabilities for each of the two classes:
    log_prob_class0 = 0
    log_prob_class1 = 0
    # The probability of a class is the product of the probabilities
    # associated with each of the feature values.
    # Because we are using logs, we add instead of multiplying
    # (otherwise it gets too small)
    for xi, t0, t1 in zip(features, theta0, theta1):
        log_prob_class0 += math.log(t0 if xi == 1 else 1 - t0)
        log_prob_class1 += math.log(t1 if xi == 1 else 1 - t1)

    # Return the most likely class (the one with the biggest probability)
    if log_prob_class0 > log_prob_class1:
        return 0
    else:
        return 1