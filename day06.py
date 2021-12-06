#!/usr/bin/env python
def read_input():
    with open("./inputs/day06") as f:
        return [int(i) for i in f.readline().strip().split(",")]


def part1():
    ages = read_input()
    days = 80
    while days > 0:
        new = 0
        for i, age in enumerate(ages):
            if age == 0:
                ages[i] = 6
                new += 1
            else:
                ages[i] -= 1
        ages.extend([8] * new)
        days -= 1

    print(f"part 1: {len(ages)}")


if __name__ == "__main__":
    part1()
