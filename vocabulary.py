import os
import pickle
from collections import Counter

class Vocabulary(object):
    def __init__(self, dump_filename):
        self.dump_filename = dump_filename
        self.word_to_index = {}
        self.index_to_word = []
        self.counter = Counter()
        self.reset()

        if os.path.isfile(self.dump_filename):
            self.load()

    def save(self):
        with open(self.dump_filename, "wb") as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def load(self):
        with open(self.dump_filename, "rb") as f:
            vocab = pickle.load(f)
            self.__dict__.update(vocab.__dict__)

    def add_word(self, word):
        self.counter[word] += 1
        if self.word_to_index.get(word) is None:
            self.index_to_word.append(word)
            index = len(self.index_to_word) -1
            self.word_to_index[word] = index
            return index
        return self.word_to_index[word]

    def get_word_index(self, word):
        if self.word_to_index.get(word) is not None:
            return self.word_to_index[word]
        return len(self.word_to_index)

    def get_word(self, index):
        return self.index_to_word[index]

    def size(self):
        return len(self.index_to_word)
    
    def reset(self):
        self.word_to_index = {}
        self.index_to_word = []
        self.counter = Counter()
        self.word_to_index["NotAWord"] = 0
        self.index_to_word.append("NotAWord")
        self.counter["NotAWord"] = 1
    
    def shrink(self, num):
        pairs = self.counter.most_common(num)
        self.reset()
        for word, count in pairs:
            self.add_word(word)