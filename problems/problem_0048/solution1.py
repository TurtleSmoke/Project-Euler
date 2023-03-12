def self_powers():
    return sum(i**i for i in range(1, 1001)) % 10**10


if __name__ == "__main__":
    print(self_powers())
