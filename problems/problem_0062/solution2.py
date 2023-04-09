import itertools
from collections import defaultdict


def cubic_permutations():
    permutations = defaultdict(list)
    for cube in (i**3 for i in itertools.count(1)):  # Condition 1
        ordered_digits = "".join(sorted(str(cube)))
        permutations[ordered_digits].append(cube)  # Condition 2
        if len(permutations[ordered_digits]) >= 5:  # Condition 3
            return min(permutations[ordered_digits])


if __name__ == "__main__":
    print(cubic_permutations())
