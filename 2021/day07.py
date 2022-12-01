#!/usr/bin/env python
from collections import defaultdict


def read_input():
    with open("./inputs/day07") as f:
        return [int(i) for i in f.readline().strip().split(",")]


def fuel(exp=False):
    crabs = read_input()
    moves = defaultdict(int)

    for crab in crabs:
        for pos in range(min(crabs), max(crabs) + 1):
            _fuel = abs(pos - crab)
            moves[pos] += _fuel if not exp else sum(range(1, _fuel + 1))

    return min(moves.values())


if __name__ == "__main__":
    print(f"part 1: {fuel()}")
    print(f"part 2: {fuel(exp=True)}")
