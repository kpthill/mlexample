from my_utils import *

def train(file):
    word_counts, label_counts = count_words(file)

    n = sum(label_counts.values()) # the total number of training set examples
    k = len(label_counts)          # the number of label values

    # P(word | label)
    word_scores = {}
    for label in word_counts:
        word_scores[label] = {}
        for word in word_counts[label]:
            # (note +1/+k for laplace smoothing)
            word_scores[label][word] = (word_counts[label][word] + 1) / (label_counts[label] + k + 0.0)

    # P(label)
    label_scores = {}
    for label in label_counts:
        label_scores[label] = label_counts[label] / (n + 0.0)

    return (word_scores, label_scores, n)

def classify(model, sentence):
    word_scores, label_scores, n = model
    words = get_words(sentence)
    posterior = {}
    total = 0

    # P(sentence | label) * P(label)
    for label in label_scores:
        product = 1
        for word in words:
            if word not in word_scores[label]:
                product *= 1.0/n
            else:
                product *= word_scores[label][word]
        posterior[label] = product * label_scores[label]
        total += posterior[label]

    best = ("", -1)

    # Normalize and find the maximum P(label|sentence)
    for label in posterior:
        posterior[label] = posterior[label] / total
        if posterior[label] > best[1]:
            best = (label, posterior[label])

    return best

# with open('../../MLexample/movie-reviews-dataset.tsv') as file:
#     mymodel = naive_bayes(file)
#
# alist = sorted(mymodel[0]['negative'].items(), key=lambda(t): -t[1])[0:10]
# print alist
# print mymodel[1]
#
# print "terrible %.19f" % mymodel[0]['positive']['terrible']
# print "terrible %.19f" % mymodel[0]['negative']['terrible']
# print "movie %.19f" % mymodel[0]['positive']['movie']
# print "movie %.19f" % mymodel[0]['negative']['movie']
#
# print classify(mymodel, "terrible movie")
