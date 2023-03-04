def read_file(filename):
    with open(filename, "r") as f:
        return [word.strip('"') for word in f.read().split(",")]
