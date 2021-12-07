#!/usr/bin/env python
from collections import defaultdict


def read_input():
    with open("./inputs/day07") as f:
        return [int(i) for i in f.readline().strip().split(",")]


def part1():
    crabs = read_input()
    moves = defaultdict(int)
    positions = range(min(crabs), max(crabs) + 1)

    for crab in crabs:
        for p in positions:
            moves[p] += abs(p - crab)
    fuel = min(moves.values())

    print(f"part 1: {fuel}")


if __name__ == "__main__":
    part1()
