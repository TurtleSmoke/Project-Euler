# Brute force

The problem gave us a file with quoted words separated by commas.
The first step is to read the file and split the words into a list.

From [read_file.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0042/read_file.py):

```python
def read_file(filename):
    with open(filename, "r") as f:
        return [word.strip('"') for word in f.read().split(",")]
```

Subsequently, we need to check if the word is a triangle word.
A word is considered a triangle word if the sum of the alphabetical position of its letters is a triangle number.
A triangle number is defined by the formula \\( \frac{1}{2}n(n+1) \\), but we are interested in finding the \\( n \\) that satisfies this formula.
To solve it, we can use the equation:

\\[
x = \frac{1}{2}n(n+1) \Rightarrow n^2 + n - 2x = 0 \Rightarrow n = \frac{\pm \sqrt{1 + 8x} - 1}{2}
\\]

The negative solution \\( \frac{- \sqrt{1 + 8x} - 1}{2} \\) can be disregarded since we are only interested in positive integers.
We can determine if \\( x \\) is a triangle number by checking if the value of \\( \frac{\sqrt{1 + 8x} - 1}{2} \\) is an integer.
Which can be done easily using the [is_integer](https://docs.python.org/3/library/stdtypes.html#float.is_integer) python function.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0042/solution1.py):

```python
def is_triangle_number(x):
    return (((1 + 8 * x) ** 0.5 - 1) / 2).is_integer()
```

Finally, we can iterate over each word in the list, calculate its value, and verify if it is a triangle number.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0042/solution1.py):

```python
def coded_triangle_numbers():
    words = read_file("words.txt")
    return sum(is_triangle_number(sum(ord(c) - ord("A") + 1 for c in word)) for word in words)
```
