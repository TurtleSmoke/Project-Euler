from math import prod
from read_file import read_file


def largest_product_in_series(n, adj=13):
    res = 0
    for i in range(len(n) - adj):
        res = max(prod(int(digit) for digit in n[i: i + adj]), res)

    return res


if __name__ == "__main__":
    print(largest_product_in_series(read_file("given.txt")))
