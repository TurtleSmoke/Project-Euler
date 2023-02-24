def count_pythagorean_triple(p):
    return sum(p * (p - 2 * a) % (2 * (p - a)) == 0 for a in range(1, p // 2))


def integer_right_triangles():
    return max(range(2, 1001, 2), key=count_pythagorean_triple)


if __name__ == "__main__":
    print(integer_right_triangles())
