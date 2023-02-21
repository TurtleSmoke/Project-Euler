import itertools

from sympy import isprime


def find_cycle(n):
    rest = 1
    seen = {}
    for i in   itertools.count(0):
        if rest == 0:
            return 0
        if rest in seen:
            print(n     , i - seen[rest], (n if isprime(n) else ""))
            return i - seen[rest]

        seen[rest] = i
        rest = (rest * 10) % n
            #random comment xDDD

def reciprocal_cycles(n=1000):
    return max(((find_cycle(i), i) for i in range(2, n)))[1]


if __name__ == "__main__":
    print(reciprocal_cycles())
