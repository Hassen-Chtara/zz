import random
import sys


def get_random_slice(x: bytes) -> bytes:
    index_ = random.randint(0, len(x) - 1)
    slice_len = random.randint(1, len(x) - index_)
    return x[index_ : index_ + slice_len]


def bit_flip(x: bytes) -> bytes:
    index_ = random.randint(0, len(x) - 1)
    mask = 1 << random.randint(0, 7)
    return x[:index_] + bytes([x[index_] ^ mask]) + x[index_ + 1 : len(x)]


def byte_flip(x: bytes) -> bytes:
    index_ = random.randint(0, len(x) - 1)
    return x[:index_] + bytes([x[index_] ^ 0xFF]) + x[index_ + 1 : len(x)]


def bytes_reversing(x: bytes) -> bytes:
    return x[::-1]


def byte_duplication(x: bytes) -> bytes:
    random_byte = random.choice(x)
    index_ = random.randint(0, len(x) - 1)
    return (
        x[:index_]
        + bytes([random_byte]) * random.randint(0, len(x) // 2)
        + x[index_ + 1 : len(x)]
    )


def byte_deletion(x: bytes) -> bytes:
    index_ = random.randint(0, len(x) - 1)
    return x[:index_] + x[index_ + 1 : len(x)]


def byte_change(x: bytes) -> bytes:
    index_ = random.randint(0, len(x) - 1)
    return x[:index_] + random.randbytes(1) + x[index_ + 1 : len(x)]


def byte_insertion(x: bytes) -> bytes:
    index_ = random.randint(0, len(x) - 1)
    return x[:index_] + random.randbytes(1) + x[index_ : len(x)]


def shuffling(x: bytes) -> bytes:
    x_ = list(x)
    random.shuffle(x_)
    return b"".join([i.to_bytes(1, sys.byteorder) for i in x_])


def inject_bytes(x: bytes) -> bytes:
    index_ = random.randint(0, len(x) - 1)
    return (
        x[:index_] + random.randbytes(random.randbytes(1)[0]) + x[index_ + 1 : len(x)]
    )
