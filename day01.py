#!/usr/bin/env python
from collections import defaultdict


def read_input():
    with open('./inputs/day01') as f:
        return f.readlines()


def part1():
    elf_num = 0
    calories = defaultdict(int)

    for v in read_input():
        v = v.strip()
        if not v:
            elf_num += 1
            continue

        calories[elf_num] += int(v)

    max_cal = max(calories.values())
    print(f'part 1: {max_cal}')



if __name__ == '__main__':
    part1()
