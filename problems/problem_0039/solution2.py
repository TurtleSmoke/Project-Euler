def count_pythagorean_triple(p):
    count = 0
    for a in range(1, p):
        for b in range(1, a):
            c = p - a - b
            if a * a + b * b == c * c:
                count += 1
    return count


def integer_right_triangles():
    return max(range(2, 1001, 2), key=count_pythagorean_triple)


if __name__ == "__main__":
    print(integer_right_triangles())
