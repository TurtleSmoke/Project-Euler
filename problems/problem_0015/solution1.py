def lattice_paths(up=20, down=20):
    moves_down = lattice_paths(up, down - 1) if down > 1 else 1
    moves_up = lattice_paths(up - 1, down) if up > 1 else 1

    return moves_up + moves_down


if __name__ == "__main__":
    print(lattice_paths())
