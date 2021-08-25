def special_pythagorean_triplet():
    for a in range(1001):
        for b in range(a + 1, 1001):
            for c in range(b + 1, 1001):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    return a * b * c

    return -1


if __name__ == "__main__":
    print(special_pythagorean_triplet())
