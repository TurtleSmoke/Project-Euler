from math import factorial


def lattice_paths(n=20):
    return factorial(2 * n) // (factorial(n) ** 2)


if __name__ == "__main__":
    print(lattice_paths())
