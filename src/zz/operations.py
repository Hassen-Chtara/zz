import random 
import sys

def bit_flip(x):
    pass

def byte_flip(x):
    pass

def bytes_reversing(x):
    return x[::-1]

def byte_duplication(x):
    pass

def byte_deletion(x):
    index_ = random.randint(0,len(x))
    return x[:index_] + x[index_+1:len(x)]

def byte_insertion(x):
    index_ = random.randint(0,len(x))
    return x[:index_ ] + random.randbytes(1) + x[index_ +1:len(x)]

def byte_shuffling(x):
    x_ = list(x)
    random.shuffle(x_)
    return b''.join([ i.to_bytes(1, sys.byteorder) for i in  x_])