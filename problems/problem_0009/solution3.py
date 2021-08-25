def special_pythagorean_triplet():
    for m in range(16, 24):
        for n in range(1, m):
            if m * (n + m) == 500:
                return 2 * m * n * (m**4 - n**4)

    return -1


if __name__ == "__main__":
    print(special_pythagorean_triplet())
