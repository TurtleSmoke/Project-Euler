def square_root_convergents():
    pn = 1
    qn = 1
    count = 0
    for _ in range(1000):
        pn, qn = 2 * qn + pn, qn + pn
        if len(str(pn)) > len(str(qn)):
            count += 1
    return count


if __name__ == "__main__":
    print(square_root_convergents())
