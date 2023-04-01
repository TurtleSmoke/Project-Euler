def read_file(filename):
    with open(filename, "r") as file:
        return [line.split() for line in file.read().splitlines()]
