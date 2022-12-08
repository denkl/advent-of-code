#!/usr/bin/env python
import functools
import operator


def read_input():
    with open('./inputs/day08') as f:
        return [l.strip() for l in f.readlines()]


def get_grid():
    grid = []
    for line in read_input():
        grid.append([int(i) for i in line])

    return grid


def visible():
    grid = get_grid()
    visible = 0

    for ri, row in enumerate(grid):
        if ri in (0, len(grid) - 1):
            visible += len(grid)
            continue

        for ci, col in enumerate(row):
            if ci in (0, len(row) - 1):
                visible += 1
                continue

            for lookup in (
                grid[ri][:ci],
                grid[ri][ci+1:],
                [grid[i][ci] for i in range(0, ri)],
                [grid[i][ci] for i in range(ri+1, len(grid))],
            ):
                if max(lookup) < col:
                    visible += 1
                    break

    return visible




def scenic():
    grid = get_grid()

    def get_score(v, pairs):
        score = 0
        for ri, ci in pairs:
            score += 1
            if grid[ri][ci] >= v:
                break
        return score

    highest = 0
    for ri, row in enumerate(grid):
        for ci, col in enumerate(row):
            left = [(ri, i) for i in range(ci-1, -1, -1)]
            right = [(ri, i) for i in range(ci+1, len(row))]
            top = [(i, ci) for i in range(ri-1, -1, -1)]
            bottom = [(i, ci) for i in range(ri+1, len(grid))]
            score = functools.reduce(
                operator.mul,
                (get_score(col, pairs) for pairs in (left, right, top, bottom))
            )
            highest = max((highest, score))

    return highest


def part1():
    print(f'part 1: {visible()}')


def part2():
    print(f'part 1: {scenic()}')


if __name__ == '__main__':
    part1()
    part2()
