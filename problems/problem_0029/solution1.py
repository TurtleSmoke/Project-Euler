def distinct_powers(n=100):
    return len({a ** b for a in range(2, n + 1) for b in range(2, n + 1)})


if __name__ == "__main__":
    print(distinct_powers())
