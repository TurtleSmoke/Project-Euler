def read_file(filename):
    with open(filename, 'r') as file:
        return [int(line) for line in file.read().split('\n')[:-1]]
