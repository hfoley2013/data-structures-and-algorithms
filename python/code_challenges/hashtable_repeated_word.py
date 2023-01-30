from data_structures.hashtable import Hashtable


def first_repeated_word(string):
    punc = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    words = string.lower().split()
    ht = Hashtable()
    for word in words:
        word = ''.join(c for c in word if c not in punc)
        if ht.has(word):
            return word
        ht.set(word, True)
    return None
