# zz - Simple Python Mutator

## Introduction

`zz` is a lightweight Python library for mutating input data, ideal for small fuzzers or testing purposes during early project development.

## Features

- Mutation of input data using various strategies.
- Easy integration into existing Python projects.
- Customizable mutation strategies.

## Usage

Using `zz` is simple. Here's a basic example:

```python
from zz import Mutator

# Create a Mutator instance
mutator = Mutator()

# Mutate some input data
mutated_data = mutator.mutate(b'original_data')

print(mutated_data)
```
## Mutation Strategies

`zz` offers basic mutation strategies such as byte flipping, bit flipping, insertion, deletion, and swapping adjacent bytes. You can also define custom mutation strategies.

## License

This project is licensed under the MIT License.