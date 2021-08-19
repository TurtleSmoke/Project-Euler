def is_evenly_divisible(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True


def smallest_multiple():
    i = 1
    while not is_evenly_divisible(i):
        i += 1
    return i


if __name__ == "__main__":
    print(smallest_multiple())
