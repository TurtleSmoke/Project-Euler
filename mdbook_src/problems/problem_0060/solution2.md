# Clique's graph theory

Another solution is to use the [clique](https://en.wikipedia.org/wiki/Clique_(graph_theory)) graph theory.
A clique is a subset of vertices in an undirected graph, such that every two distinct vertices in the clique are adjacent.
In this problem, a graph can be defined with vertices representing primes and edges representing the concatenation of two primes being prime.
The solution can be found by finding the clique of size 5 with the smallest sum.
Indeed, a clique of size 5 is a set of 5 vertices (primes) such that every two vertices are adjacent (every concatenation of two primes is prime).

To simplify the process of creating the graph and finding the clique, the [networkx](https://networkx.github.io/) library is used.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0060/solution2.py):

```python
def prime_pair_sets():
    primes = list(sieve.primerange(10000))
    pairs = ((p1, p2) for p1 in primes for p2 in primes if p1 < p2 and concat(p1, p2))
    graph = nx.Graph()
    graph.add_edges_from(pairs)
    five_cliques = [sum(clique) for clique in find_cliques(graph) if len(clique) == 5]
    return sorted(five_cliques)[0]
```
