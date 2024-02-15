from zz import Mutator


mut = Mutator()
mut.load_to_corpus('test_corpus')
print(mut.mutate())
print(mut.mutate())
print(mut.mutate())
print(mut.mutate())
print(mut.mutate())
