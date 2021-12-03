#!/usr/bin/env python
def part1():
    with open("./inputs/day03") as f:
        report = f.readlines()

    nbits = len(report[0].strip())
    ones = [0] * nbits
    for line in report:
        bits = [int(i) for i in line.strip()]
        for i, bit in enumerate(bits):
            if bit:
                ones[i] += 1

    gamma = "".join("1" if c > (len(report) / 2) else "0" for c in ones)
    epsilon = "".join("1" if c == "0" else "0" for c in gamma)
    power = int(gamma, 2) * int(epsilon, 2)
    print(f"part 1: {power}")


if __name__ == "__main__":
    part1()
