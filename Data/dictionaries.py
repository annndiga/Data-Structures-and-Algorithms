import string


def word_frequency(sentence):
    words = sentence.lower().split()
    words = [word.strip(string.punctuation) for word in words]
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency