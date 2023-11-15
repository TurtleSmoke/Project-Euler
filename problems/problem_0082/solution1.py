from read_file import read_file


def path_sum_three_ways(filename=".txt"):
    rows = read_file(filename)
    current = [r[0] for r in rows]

    for x in range(1, len(rows[0])):
        for y in range(len(rows)):  # Left to right
            current[y] += rows[y][x]
        print(current)
        for y in range(1, len(rows)):  # Top to bottom
            current[y] = min(current[y], current[y - 1] + rows[y][x])
        for y in range(len(rows) - 2, -1, -1):  # Bottom to top
            current[y] = min(current[y], current[y + 1] + rows[y][x])

    return min(current)


if __name__ == "__main__":
    print(path_sum_three_ways())
