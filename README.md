
# ZZ - Simple Python Mutator


`zz` is a lightweight Python package for mutating bytes, ideal for small projects where byte mutation is needed.

## Features

- Mutation of bytes using various strategies.
- Easy integration into existing Python projects.
- Customizable mutation strategies.

## Usage

Using `zz` is simple. Here's a basic example:

```python
from zz import Mutator

# Create a ByteMutator instance
mutator = Mutator()

# Mutate some bytes
mutated_bytes = mutator.mutate(b'original_bytes')

print(mutated_bytes)
```

## Mutation Strategies

`zz` offers basic mutation strategies such as byte flipping, bit flipping, insertion, deletion, and swapping adjacent bytes. You can also define custom mutation strategies.

## Examples

### Fuzz Testing

```python
from zz import ByteMutator

# Create a ByteMutator instance
mutator = ByteMutator()

# Fuzz testing example
original_bytes = b'some_input_bytes'

for _ in range(10):
    mutated_bytes = mutator.mutate(original_bytes)
    # Perform testing with mutated_bytes
```

## License

This project is licensed under the MIT License.
