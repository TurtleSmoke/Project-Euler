# Topological sorting

## Problem:

We need to to find the shortest passcode based on a series of samples containing three random characters chosen in order.

## Understanding the problem

For example, if the samples are \\( 145 \\), \\( 456\\) and \\( 146 \\), we can infer certain order constraints, like \\( 1 \\) must be before \\( 4 \\), \\( 4 \\) before \\( 5 \\), and so on.
We also know that \\( 1 \\) is before \\( 5 \\), but it would be redundant since we already know that \\( 1 \\) is before \\( 4 \\) and \\( 4 \\) is before \\( 5 \\).

We can represent these constraints as a directed graph, where the nodes are the characters and the edges describe the constraints, i.e. if there is an edge \\( a \rightarrow b \\), then \\( a \\) is before \\( b \\).
For the previous example, the graph would be:

<p align="center">
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="332pt" height="67pt" viewBox="0.00 0.00 332.00 67.00">
        <use href="../../images/p0079/p0079-s1-ex-graph.svg#graph"> </use>
    </svg>
</p>

From this graph, it's clear that the shortest passcode is \\( 1456 \\).
But what if the graph was more complex?
If it was, we would need some algorithm to find the solution, and that is where [topological sorting](https://en.wikipedia.org/wiki/Topological_sorting) comes in handy.

## Solution


The first step is to read the file:

From [read_file.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0079/read_file.py):

```python
def read_file(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()
```

Then, we can compute the graph.
I chose to represent the graph as a dictionary of sets, where the keys are the nodes and the values the connected nodes.
Using the previous example, the graph would be represented as:

```python
{
    '1': {'4'},
    '4': {'5', '6'},
    '5': {'6'},
}
```

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0079/solution1.py):

```python
def compute_graph(char):
    graph = defaultdict(set)
    for a, b, c in char:
        graph[a].add(b)
        graph[b].add(c)

    return graph
```

Using some visualization, here's what the graph looks like with the real data:

<p align="center">
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="692pt" height="317pt" viewBox="0.00 0.00 692.00 317.14">
        <use href="../../images/p0079/p0079-s1-full-graph.svg#graph"> </use>
    </svg>
</p>

Quite tentacular, but we can still guess the passcode: \\( 73162890 \\).
For the topological sorting, I've opted to use [depth-first search](https://en.wikipedia.org/wiki/Depth-first_search) since it's the easiest to implement.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0079/solution1.py):

```python
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
```

Finally, we merge everything together to obtain the solution:

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0079/solution1.py):

```python
def passcode_derivation(filename="keylog.txt"):
    chars = read_file(filename)
    graph = compute_graph(chars)
    passcode = topological_sort(graph)
    return "".join(passcode)
```

The passcode is indeed \\( 73162890 \\).

If you understood the solution, you might have noticed that we assumed that the graph is [acyclic](https://en.wikipedia.org/wiki/Cycle_(graph_theory)), meaning it has no cycles.
In our case, this implies that there is no redundant numbers in the passcode.
If there were cycles, finding the passcode would be more challenging... Maybe it will be the subject of another solution?