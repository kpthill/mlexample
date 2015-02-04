from numpy import *
from my_utils import *

alpha = 2
threshold = 0.05

testing = False
def debug(msg):
    if testing:
        print msg

def train(data):
    return gradient_ascent(data)

def gradient_ascent(data):
    data = list(data)
    theta = {}
    error = threshold + 1
    i = 0
    while i < 50:
        i += 1
        print "starting gradient ascent."
        error = 0
        n = 0

        for line in data:
            n += 1
            label, sentence = line.split('\t', 1)
            words = get_words(sentence)
            y = 1 if label == 'positive' else 0
            score = score_sentence(theta, words)
            for word in words:
                if word not in theta:
                    theta[word] = 0
                theta[word] += alpha * (y - score)
            error += math.fabs(y - score)

        error = error / n
        print error
    return theta

def score_sentence(theta, words):
    res = 0
    for word in words:
        if word in theta:
            res += theta[word] # this is theta[i]*x[i] since the x's are 0 or 1 valued
    return sigmoid(res)

def sigmoid(num):
    return 1.0 / (1 + math.exp(-num))

def classify(model, sample):
    res = 0;
    words = get_words(sample)

    debug( words)

    for word in words:
        if word in model:
            debug( "%s: %f" % (word, model[word]))
            res += model[word]
        else:
            continue

    debug( res)

    label = 'positive' if sigmoid(res) > 0.5 else 'negative'

    answer = label, sigmoid(res)

    debug( answer)
    return answer

if __name__ == "__main__":
    with open('../../MLexample/movie-reviews-dataset.tsv') as file:
        mymodel = train(list(file))
        print sorted(mymodel.items(), key=lambda(t):-t[1])[0:10]
        print classify(mymodel, "captain destructo is a dull and lifeless film, scraping by only by a base appeal to our most atavistic instincts")
        print mymodel['and']
        counts = {'positive':0, 'negative':0}
        for line in file:
            label, sentence = line.split('\t', 1)
            words = get_words(sentence)
            if 'and' in words:
                counts[label] += 1

        print counts
