# Tree of primitive Pythagorean triples

The [Even fewer loops](./solution3.md) solution is already fast, but we can continue to improve it.
Indeed, Pythagorean triples are a generalization of a special case called [primitive Pythagorean triples](https://en.wikipedia.org/wiki/Pythagorean_triple#Primitive_Pythagorean_triple), where \\( a \\), \\( b \\) and \\( c \\) are coprime.
There exists multiple ways to generate them, such as the [Euclid's formula](https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple).

I prefer the [Tree of primitive Pythagorean triples](https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples) method.
This method is based on the fact that all primitive Pythagorean triples has the structure of a tree.
We start with the root \\( (3, 4, 5) \\), which is the first primitive pythagorean triples, and then recursively generate the children of each node by multiplying it by a matrix \\( A \\), \\( B \\) or \\( C \\).

\\( A \\), \\( B \\) and \\( C \\) that are defined as:
\\[
A = \begin{bmatrix}
1 & -2 & 2 \\\\
2 & -1 & 2 \\\\
2 & -2 & 3 \\\\
\end{bmatrix},
B = \begin{bmatrix}
1 & 2 & 2 \\\\
2 & 1 & 2 \\\\
2 & 2 & 3 \\\\
\end{bmatrix},
C = \begin{bmatrix}
-1 & 2 & 2 \\\\
-2 & 1 & 2 \\\\
-2 & 2 & 3 \\\\
\end{bmatrix}
\\]

In our case we are also interested in the non-primitive Pythagorean triples.
To generate these triples, we can start with a primitive Pythagorean triple like \\( a,b,c \\) and multiply each value by a positive integer.
This will create a new triplet \\( (k \times a, k \times b, k \times c) \\) with perimeter \\( p = k \times (a + b + c) \\).
The limit of this multiplication factor \\( k \\) is restricted by \\( p \\) being less than \\( 1000 \\).

To put it all together, we can write a recursive function that will generate all the primitive Pythagorean triples with perimeter less than \\( 1000 \\).
From there, we can generate all the Pythagorean triples with perimeter less than \\( 1000 \\).
We will use [numpy](https://numpy.org/) to represent the matrices and perform the multiplication.

From [solution4.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0039/solution4.py):

```python
def compute_all_pythagorean_triples(results, max_p, abc):
    curr_p = sum(abc)
    if curr_p < max_p:
        for perimeter in range(curr_p, max_p, curr_p):
            results[perimeter] += 1
        compute_all_pythagorean_triples(results, max_p, A @ abc)
        compute_all_pythagorean_triples(results, max_p, B @ abc)
        compute_all_pythagorean_triples(results, max_p, C @ abc)
```

Finally, we can count the number of solutions for each perimeter and return the one with the maximum number of solutions.

From [solution4.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0039/solution4.py):

```python
def integer_right_triangles():
    results = defaultdict(int)
    compute_all_pythagorean_triples(results, 1001, np.array([3, 4, 5]))
    return max(results, key=results.get)
```
