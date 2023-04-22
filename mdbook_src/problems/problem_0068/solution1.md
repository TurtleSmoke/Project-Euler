# Brute force

The problem is to find the maximum 16-digit string for a "magic" 5-gon ring.
In this context, a "magic" gon ring is valid if all lines add up to the same number.

To solve this problem the brute force way, we need to:

#### 1. Generate all possible rings.

There exists multiple possible representation of a ring, one simple approach is to use a list where the first elements are the inner ring and the last five elements are the outer ring in clockwise order.
Generating every possible rings can be easily done using `itertools.permutations`.

#### 2. Check if each ring is valid.

To validate a "magic" gon ring, it is enough to check if all lines add up to the same number.
The \\( i \\)-th line is the sum of the \\( i \\)-th element of the inner ring, the \\( i + 1 \\)-th element of the inner ring, and the \\( i \\)-th element of the outer ring.
If all lines have the same sum, then the ring is valid.
This is checked by verifying that the set of line sums has only one element.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0068/solution1.py):

```python
def is_gon_valid(inner, outer):
    return len(set(inner[i] + inner[(i + 1) % 5] + outer[i] for i in range(5))) == 1
```

#### 3. Check if each ring is a 16-digit string.

The string representation of a ring is the concatenation of each line, starting with the lowest external node and reading clockwise.
Each line is represented by the concatenation of the outer node, and the two inner nodes.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0068/solution1.py):

```python
def ring_to_string(inner, outer):
    start = outer.index(min(outer))
    return "".join((str(outer[i % 5]) + str(inner[i % 5]) + str(inner[(i + 1) % 5]) for i in range(start, start + 5)))
```

Finding string of length 16 is trivial.

#### 4. Find the maximum 16-digit string.

The maximum 16-digit string can be found using `max` built-in function, as it performs a lexicographical comparison.

The rest is to put it all together.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0068/solution1.py):

```python
def magic_5_gon_ring():
    all_gons = itertools.permutations(range(1, 11))  # Condition 1
    valid_gons = filter(lambda gon: is_gon_valid(gon[:5], gon[5:]), all_gons)  # Condition 2
    string_gons = map(lambda gon: ring_to_string(gon[:5], gon[5:]), valid_gons)
    string_gons = filter(lambda gon: len(gon) == 16, string_gons)  # Condition 3
    res = max(string_gons)  # Condition 4
    return res
```
