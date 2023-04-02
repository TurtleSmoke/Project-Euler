def is_lychrel(n):
    for _ in range(50):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True


def lychrel_numbers():
    return sum(is_lychrel(n) for n in range(1, 10000))


if __name__ == "__main__":
    print(lychrel_numbers())
