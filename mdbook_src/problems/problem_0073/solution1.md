# Brute force

The problem is to find the number of reduced proper fractions \\( \\frac{n}{d} \\) such that \\( \\frac{1}{3} < \\frac{n}{d} < \\frac{1}{2} \\) and \\( n \\) and \\( d \\) are coprime.
A brute force solution generates all Farey sequences between \\( \\frac{1}{3} \\) and \\( \\frac{1}{2} \\) and counting the number of fractions in each sequence.

The Stern-Brocot tree can be used to generate Farey sequences.
Starting from two adjacent fractions \\( \\frac{a}{b} \\) and \\( \\frac{c}{d} \\), the mediant \\( \\frac{a+c}{b+d} \\) is also in the Farey sequence.
This process can be repeated with the left fraction and the mediant, and the right fraction and the mediant, and so on.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0073/solution1.py):

```python
def stern_brocot_tree(a, b, c, d):
    if b + d > 12000:
        return 0

    return 1 + stern_brocot_tree(a, b, a + c, b + d) + stern_brocot_tree(a + c, b + d, c, d)
```

To solve the problem, the rest is to initialize the tree with the fractions \\( \\frac{1}{3} \\) and \\( \\frac{1}{2} \\), and count the number of fractions in the Farey sequence between them.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0073/solution1.py):

```python
def counting_fractions_in_a_range():
    return stern_brocot_tree(1, 3, 1, 2)
```

It is worth noting that the Python default recursion limit may need to be increased for this solution to work.
