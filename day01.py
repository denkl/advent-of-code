#!/usr/bin/env python
from collections import defaultdict
import heapq


def read_input():
    with open('./inputs/day01') as f:
        return f.readlines()


def _calories_per_elf():
    elf_num = 0
    calories = defaultdict(int)

    for v in read_input():
        v = v.strip()
        if not v:
            elf_num += 1
            continue

        calories[elf_num] += int(v)

    return calories


def part1():
    max_cal = max(_calories_per_elf().values())
    print(f'part 1: {max_cal}')


def part2():
    top_three = sum(sorted(_calories_per_elf().values())[-3:])
    print(f'part 2: {top_three}')



if __name__ == '__main__':
    part1()
    part2()
