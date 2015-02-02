from numpy import *
from my_utils import *

alpha = 1
threshold = #?????

def train(data):


def gradient_ascent(data):
    error = threshold
    while error > threshold:
        error = 0
        for line in data:
            label, sentence = line.split('\t', 1)
            words = get_words(sentence)
            y = 1 if label == 'positive' else 0
            score = score_sentence(theta, words)
            for word in words:
                theta[word] += alpha * (y - score)
            error += y - score
    return theta

def score_sentence(theta, words):
    res = 0
    for word in words:
        if word in theta:
            res += theta[word] # this is theta[i]*x[i] since the x's are 0 or 1 valued
    return sigmoid(res)

def sigmoid(num):
    return 1.0 / (1 + math.exp(num))

def classify(model, sample):
    res = 0;
    for word in words:
        res += theta[word]

    label = 'positive' if res > 0 else 'negative'

    return label, sigmoid(res)
