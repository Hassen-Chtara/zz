from .operations.bytes import *
import os


class Mutator:
    def __init__(self, corpus=set(), dictionary=set()):
        self.corpus = corpus
        self.dictionary = dictionary

    def is_corpus_empty(self):
        return not self.corpus

    def is_dictionary_empty(self):
        return not self.dictionary

    def add_to_corpus(self, x):
        self.corpus.add(x)

    def add_to_dictionary(self, x):
        self.dictionary.add(x)

    def get_random_seed(self):
        return random.choice(list(self.corpus))

    def load_to_corpus(self, path):
        if os.path.isfile(path):
            self.load_file_to_corpus(path)
        self.load_directory_to_corpus(path)

    def load_file_to_corpus(self, path):
        with open(path, "rb") as f:
            self.add_to_corpus(f.read())

    def load_directory_to_corpus(self, path):
        files = [
            os.path.join(path, f)
            for f in os.listdir(path)
            if os.path.isfile(os.path.join(path, f))
        ]
        for file in files:
            self.load_file_to_corpus(file)

    def select_seed(self, seed):
        if seed:
            x_ = seed
        elif not self.is_corpus_empty():
            x_ = self.get_random_seed()
        else:
            raise (
                "No seed to mutate!! mutate() expectes an input or a value in the courpus"
            )
        return x_