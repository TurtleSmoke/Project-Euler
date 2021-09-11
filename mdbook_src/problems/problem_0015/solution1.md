# Brute force

We are searching for the number of different paths starting from the top left
corner and going to the bottom right corner of a \\( 20 \times 20 \\)
square. The only possible moves are down and right. This is the same as
searching for the [Lattice path](https://en.wikipedia.org/wiki/Lattice_path).

Since the square is \\( 20 \times 20 \\) we have 20 moves down and 20 moves to
the right. If we move to the right, then we have 20 moves down and 19 moves to
the right, we can continue as long as we have moves available.

The solution can be done recursively, starting with 20 moves down and right, the
result being the combination of paths down and to the right. Each times we move
down we call the function recursively with the same number of moves to the
right, but one less move down. When the number of move down is 1, the result is
obviously 1: the only remaining path is the one to the right. The same can be
done for the move to the right.

From [solution1.py](https://github.com/turtlesmoke/project-euler/blob/main/problems/problem_0015/solution1.py):

```python
def lattice_paths(up=20, down=20):
    moves_down = lattice_paths(up, down - 1) if down > 1 else 1
    moves_up = lattice_paths(up - 1, down) if up > 1 else 1

    return moves_up + moves_down
```
