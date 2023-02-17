from math import prod
from read_file import read_file


def split_series(n):
    return [sub_n for sub_n in n.split("0") if len(sub_n) >= 13]


def largest_product_in_series(n, adj=13):
    res = 0
    current = prod(int(digit) for digit in n[0:adj])
    for i in range(len(n) - adj):
        current = (current // int(n[i])) * int(n[i + adj])
        res = max(res, current)

    return res


def largest_product_in_multiples_series(sub_n, adj=13):
    res = 0
    for n in sub_n:
        res = max(largest_product_in_series(n, adj), res)
    return res


if __name__ == "__main__":
    sub_series = split_series(read_file("given.txt"))
    print(largest_product_in_multiples_series(sub_series))
