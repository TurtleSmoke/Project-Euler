import itertools
from collections import Counter


def parse_file():
    with open("cipher.txt", "r") as f:
        return [int(x) for x in f.read().split(",")]


def xor_decryption():
    code = parse_file()
    k1 = Counter(code[::3]).most_common(1)[0][0] ^ ord(" ")
    k2 = Counter(code[1::3]).most_common(1)[0][0] ^ ord(" ")
    k3 = Counter(code[2::3]).most_common(1)[0][0] ^ ord(" ")
    key = [k1, k2, k3]
    res = [chr(c ^ p) for (c, p) in zip(parse_file(), itertools.cycle(key))]
    return sum(ord(c) for c in res)


if __name__ == "__main__":
    print(xor_decryption())
