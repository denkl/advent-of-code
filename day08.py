#!/usr/bin/env python
def read_input():
    with open('./inputs/day08') as f:
        return [l.strip() for l in f.readlines()]


def visible():
    grid = []
    for line in read_input():
        grid.append([int(i) for i in line])

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

def part1():
    print(f'part 1: {visible()}')


if __name__ == '__main__':
    part1()
