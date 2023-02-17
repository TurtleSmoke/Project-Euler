def read_file(filename):
    with open(filename, "r") as file:
        return [name[1:-1] for name in file.read().split(",")]
