#!/usr/bin/env python
def read_input():
    heightmap = []
    with open("./inputs/day09") as f:
        for line in f.readlines():
            heightmap.append([int(n) for n in line if n.isdigit()])
    return heightmap


def part1():
    heightmap = read_input()
    points = []
    h, w = len(heightmap), len(heightmap[0])

    for ri, row in enumerate(heightmap):
        for ci, col in enumerate(row):
            adj = []
            if ci > 0:
                adj.append(row[ci - 1])
            if ci < w - 1:
                adj.append(row[ci + 1])
            if ri > 0:
                adj.append(heightmap[ri - 1][ci])
            if ri < h - 1:
                adj.append(heightmap[ri + 1][ci])

            if all([col < i for i in adj]):
                points.append(col)

    risk = sum([p + 1 for p in points])
    print(f"part 1: {risk}")


if __name__ == "__main__":
    part1()
