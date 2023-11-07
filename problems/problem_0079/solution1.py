from collections import defaultdict

from read_file import read_file


def compute_graph(char):
    graph = defaultdict(set)
    for a, b, c in char:
        graph[a].add(b)
        graph[b].add(c)

    return graph


def topological_sort(graph):
    marked = set()
    result = []

    def dfs(node):
        if node not in marked:
            # Using defaultdict requires us to check if the node is in the graph
            # to prevent errors during iteration caused by unintentional key creation.
            if node in graph:
                for neighbour in graph[node]:
                    dfs(neighbour)
            marked.add(node)
            result.insert(0, node)

    for node in graph:
        dfs(node)

    return result


def passcode_derivation(filename="keylog.txt"):
    chars = read_file(filename)
    graph = compute_graph(chars)
    passcode = topological_sort(graph)
    return "".join(passcode)


if __name__ == "__main__":
    print(passcode_derivation())
