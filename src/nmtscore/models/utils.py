from typing import List, Iterable


def batch(input: List, batch_size: int) -> Iterable:
    l = len(input)
    for ndx in range(0, l, batch_size):
        yield input[ndx : min(ndx + batch_size, l)]
