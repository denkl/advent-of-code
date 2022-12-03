#!/usr/bin/env python
import string


def read_input():
    with open('./inputs/day03') as f:
        return f.readlines()


priority = {l: i for i, l in enumerate(string.ascii_letters, 1)}


def part1():
    total = 0
    for rucksack in read_input():
        half_len = len(rucksack) // 2
        first, second = rucksack[:half_len], rucksack[half_len:]
        common = set(first) & set(second)
        total += priority[next(iter(common))]
    print(f'part 1: {total}')


if __name__ == '__main__':
    part1()
