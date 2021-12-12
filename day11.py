#!/usr/bin/env python
from itertools import chain


def read_input():
    output = []
    with open("./inputs/day11") as f:
        for line in f.readlines():
            output.append([int(i) for i in line.strip()])
    return output


def step(grid):
    c = 0
    w, h = len(grid[0]), len(grid)
    flashed = set()
    to_flash = set()
    for ri, row in enumerate(grid):
        for ci, col in enumerate(row):
            if col == 9:
                to_flash.add((ri, ci))
                grid[ri][ci] = 0
            else:
                grid[ri][ci] += 1
    while to_flash:
        ri, ci = to_flash.pop()
        c += 1
        flashed.add((ri, ci))

        to_incr = set()
        if ri > 0:
            if ci > 0:
                to_incr.add((ri - 1, ci - 1))
            to_incr.add((ri - 1, ci))
            if ci < w - 1:
                to_incr.add((ri - 1, ci + 1))
        if ci > 0:
            to_incr.add((ri, ci - 1))
        if ci < w - 1:
            to_incr.add((ri, ci + 1))
        if ri < h - 1:
            if ci > 0:
                to_incr.add((ri + 1, ci - 1))
            to_incr.add((ri + 1, ci))
            if ci < w - 1:
                to_incr.add((ri + 1, ci + 1))

        for i in to_incr:
            ri, ci = i
            if grid[ri][ci] == 9:
                to_flash.add(i)
                grid[ri][ci] = 0
            elif grid[ri][ci] != 0:
                grid[ri][ci] += 1
    return c


def part1():
    grid = read_input()
    steps = 100
    count = 0
    while steps:
        count += step(grid)
        steps -= 1

    print(f"part 1: {count}")


def part2():
    grid = read_input()
    count = 0
    while True:
        step(grid)
        count += 1
        if not sum(chain.from_iterable(grid)):
            break
    print(f"part 2: {count}")


if __name__ == "__main__":
    part1()
    part2()
