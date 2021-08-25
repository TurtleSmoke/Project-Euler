def special_pythagorean_triplet():
    for a in range(501):
        for b in range(a + 1, 501):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c

    return -1


if __name__ == "__main__":
    print(special_pythagorean_triplet())
