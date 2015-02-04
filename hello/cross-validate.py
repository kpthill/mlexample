import random

training_fraction = 0.7

def cross_validate(train, classify, data):
    training_set = list(data) #[]
    test_set = list(training_set) #[]
    # for line in data:
    #     if random.random() < training_fraction:
    #         training_set.append(line)
    #     else:
    #         test_set.append(line)

    model = train(training_set)

    correct = 0
    total = len(test_set)

    for line in test_set:
        label, sample = line.split("\t", 1)
        guess = classify(model, sample)[0]
        print (label, guess, sample)
        if guess == label:
            correct += 1

    score = correct / (total + 0.0)

    return model, score

import naive_bayes
import logistic

with open('../../MLexample/movie-reviews-dataset.tsv') as dataset:
    score = cross_validate(logistic.train, logistic.classify, dataset)[1]
    print "score: %f" % score

# alist = sorted(mymodel[0]['negative'].items(), key=lambda(t): -t[1])[0:10]
# print alist
# print mymodel[1]

# print "terrible %.19f" % mymodel[0]['positive']['terrible']
# print "terrible %.19f" % mymodel[0]['negative']['terrible']
# print "movie %.19f" % mymodel[0]['positive']['movie']
# print "movie %.19f" % mymodel[0]['negative']['movie']
