def get_words(sentence):
    return set(sentence.split())

def count_words(file):
    word_counts = {}
    label_counts = {}
    for line in file:
        label, sentence = line.split("\t", 1)
        words = get_words(sentence)
        for word in words:
            if label not in word_counts:
                word_counts[label] = {}
            word_counts[label][word] = word_counts[label].get(word, 0) + 1
            label_counts[label] = label_counts.get(label, 0) + 1
    return [word_counts, label_counts]
