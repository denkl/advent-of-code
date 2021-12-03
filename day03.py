#!/usr/bin/env python
import operator
from collections import Counter


def get_report():
    with open("./inputs/day03") as f:
        lines = []
        for line in f.readlines():
            lines.append([int(bit) for bit in line.strip()])
        return lines


def part1():
    report = get_report()
    nbits = len(report[0])
    ones = [0] * nbits

    for line in report:
        for i, bit in enumerate(line):
            if bit:
                ones[i] += 1

    gamma = "".join("1" if c > (len(report) / 2) else "0" for c in ones)
    epsilon = "".join("1" if c == "0" else "0" for c in gamma)
    power = int(gamma, 2) * int(epsilon, 2)

    print(f"part 1: {power}")


def _common(bits, least=False):
    if least:
        n, default, cmp = -1, 0, operator.lt
    else:
        n, default, cmp = 0, 1, operator.gt
    bit, counts = Counter(bits).most_common()[n]
    return bit if cmp(counts, (len(bits) / 2)) else default


def _get_rating(least=False):
    rows = get_report()
    ncols = len(rows[0])

    for ncol in range(ncols):
        bits = [r[ncol] for r in rows]
        criteria = _common(bits, least=least)
        rows = [r for r in rows if r[ncol] == criteria]
        if len(rows) == 1:
            return int("".join(str(i) for i in rows[0]), 2)


def part2():
    oxygen = _get_rating()
    co2 = _get_rating(least=True)
    print(f"part 2: {oxygen * co2}")


if __name__ == "__main__":
    part1()
    part2()
