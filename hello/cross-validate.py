import random

training_fraction = 0.7

def cross_validate(train, classify, data):
    training_set = []
    test_set = []
    for line in data:
        if random.random() < training_fraction:
            training_set.append(line)
        else:
            test_set.append(line)

    model = train(training_set)

    correct = 0
    total = len(test_set)

    for line in test_set:
        label, sample = line.split("\t", 1)
        guess, percent = classify(model, sample)
        if guess == label:
            correct += 1

    score = correct / (total + 0.0)

    return model, score

import naive_bayes
import logistic

with open('../../MLexample/movie-reviews-dataset.tsv') as dataset:
    score = cross_validate(logistic.train, logistic.classify, dataset)[1]
    print "score: %f" % score
