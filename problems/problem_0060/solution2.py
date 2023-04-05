import networkx as nx
from networkx.algorithms.clique import find_cliques
from sympy import isprime, sieve


def concat(p1, p2):
    return isprime(int(str(p1) + str(p2))) and isprime(int(str(p2) + str(p1)))


def prime_pair_sets():
    primes = list(sieve.primerange(10000))
    pairs = ((p1, p2) for p1 in primes for p2 in primes if p1 < p2 and concat(p1, p2))
    graph = nx.Graph()
    graph.add_edges_from(pairs)
    five_cliques = [sum(clique) for clique in find_cliques(graph) if len(clique) == 5]
    return sorted(five_cliques)[0]


if __name__ == "__main__":
    print(prime_pair_sets())
