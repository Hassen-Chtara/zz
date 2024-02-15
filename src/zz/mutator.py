from .operations import *
import os


class Mutator :
    def __init__(self,corpus=set(),dictionary=set()):
        self.corpus = corpus
        self.dictionary = dictionary

    def is_corpus_empty(self):
        return not self.corpus

    def add_to_corpus(self,x):
        self.corpus.add(x)

    def add_to_dictionary(self,x):
        self.dictionary.add(x)

    def get_random_seed(self):
        return random.choice(list(self.corpus))

    def load_to_corpus(self,path):
        if os.path.isfile(path) :
            self.load_file_to_corpus(path)
        self.load_directory_to_corpus(path)

    def load_file_to_corpus(self,path):
        with open(path,'rb') as f:
            self.add_to_corpus(f.read())

    def load_directory_to_corpus(self,path):
        files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        for file in files :
            self.load_file_to_corpus(file)

    def mutate(self,seed=None,times=5):
        if seed :
            x_ = seed
        elif not self.is_corpus_empty() :
            x_ = self.get_random_seed()
        else :
            ## raise : no seed to mutate
            raise('No seed to mutate!! mutate() expectes an input or a value in the courpus')

        for _ in range(times) :
            operation = random.choice([bytes_reversing, byte_deletion, byte_insertion, byte_shuffling])
            x_ = operation(x_)
        return x_