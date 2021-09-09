from read_file import read_file


def large_sum(filename):
    return str(sum(read_file(filename)))[:10]


if __name__ == "__main__":
    print(large_sum("given.txt"))
