def count_words(file):
    word_counts = {}
    label_counts = {}
    for line in file:
        label, sentence = line.split("\t", 1)
        words = line.split()
        for word in words:
            if label not in word_counts:
                word_counts[label] = {}
            word_counts[label][word] = word_counts[label].get(word, 0) + 1
            label_counts[label] = label_counts.get(label, 0) + 1
    return [word_counts, label_counts]

def naive_bayes(file):
    word_counts, label_counts = count_words(file)
    n = sum(label_counts.values()) # the total number of training set examples

    word_scores = {}  # these are P(word | label)
    for label in word_counts:
        word_scores[label] = {}
        for word in word_counts[label]:
            word_scores[label][word] = word_counts[label][word] / (label_counts[label] + 0.0)

    label_scores = {} # these are P(label)
    for label in label_counts:
        label_scores[label] = label_counts[label] / (n + 0.0)

    return (word_scores, label_scores)
