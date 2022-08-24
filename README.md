# random-typing
Tools for Typing - most commonly used with timeit

## Installation

From PIP:

```
$ pip install random-typing
```

## Import module

```python
from random_typing import List, Int, Str
```

## Int

### Description

`Int` is a generator function which generates random integers

It takes two parameters:
* `min_val`: int - minimum value of random integer
* `max_val`: int - maximum value of random integer

### Example

#### Code:

```python
i = Int(1, 100)
for _ in range(10):
    print(next(i))
```

#### Output:

```python
9
93
2
85
10
10
56
39
40
48
```

## Str

### Description

`Str` is a generator function which generates random strings

It takes two parameters:
* `chars`: Iterable[str] - pool of characters to choose from when generating the string
* `length`: int - length of the string

### Example

#### Code:

```python
s = Str('abcdef', 3)
for _ in range(10):
    print(next(s))
```

#### Output:

```python
ddf
bec
dfb
bba
ecf
dfd
ded
bab
ffc
aad
```

## List

### Description

`List` is a generator function which generates random lists

It takes two parameters:
* `items`: Any - the items of the list
* `length`: int - the length of the list

### Example

#### Code:

```python
i = Int(1, 10)
l = List(i, 5)
for _ in range(10):
    print(next(l))
```

Output:

```python
[10, 1, 6, 10, 4]
[3, 8, 8, 6, 1]
[9, 3, 7, 10, 1]
[1, 6, 9, 2, 10]
[3, 10, 3, 7, 2]
[10, 2, 2, 3, 4]
[3, 7, 2, 9, 3]
[9, 10, 3, 10, 1]
[1, 7, 3, 7, 5]
[1, 1, 9, 9, 8]
```

## Usage

This can be used with `timeit`, like this:

```python
# Checking whether bubble sort is quicker than merge sort

import timeit
from random_typing import List, Int

lengths = list(range(1, 1000))
times_bubble = []
times_merge = []

i = Int(1, 100)

for length in lengths:
    l = List(i, length)
    times_bubble.append(timeit.timeit('BubbleSort(lst)',
                                      globals={'lst': next(l), 'BubbleSort': BubbleSort},
                                      number=1))
    times_merge.append(timeit.timeit('MergeSort(lst)',
                                     globals={'lst': next(l), 'MergeSort': MergeSort},
                                     number=1))
```
