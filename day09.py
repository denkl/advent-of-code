#!/usr/bin/env python
from functools import reduce


def read_input():
    heightmap = []
    with open("./inputs/day09") as f:
        for line in f.readlines():
            heightmap.append([int(n) for n in line if n.isdigit()])
    return heightmap


def get_adj(point, hw):
    ri, ci = point
    h, w = len(hw), len(hw[0])
    adj = set()
    if ci > 0:
        adj.add((ri, ci - 1))
    if ci < w - 1:
        adj.add((ri, ci + 1))
    if ri > 0:
        adj.add((ri - 1, ci))
    if ri < h - 1:
        adj.add((ri + 1, ci))
    return adj


def risk_levels_points(heightmap):
    points = []

    for ri, row in enumerate(heightmap):
        for ci, col in enumerate(row):
            adj = get_adj((ri, ci), heightmap)
            if all([col < heightmap[ari][aci] for ari, aci in adj]):
                points.append((ri, ci))

    return points


def part1():
    heightmap = read_input()
    points = risk_levels_points(heightmap)
    risk = sum([heightmap[ri][ci] + 1 for ri, ci in points])
    print(f"part 1: {risk}")


def part2():
    heightmap = read_input()
    low_points = risk_levels_points(heightmap)

    seen = set()
    basins = []
    for point in low_points:
        basin = set()
        adj_locs = set()
        adj_locs.add(point)

        while adj_locs:
            adj_p = adj_locs.pop()
            seen.add(adj_p)
            ri, ci = adj_p
            if heightmap[ri][ci] == 9:
                continue
            basin.add(adj_p)
            for i in get_adj(adj_p, heightmap):
                if i not in seen:
                    adj_locs.add(i)

        basins.append(len(basin))

    res = reduce(lambda x, y: x * y, sorted(basins, reverse=True)[:3])
    print(f"part 2: {res}")


if __name__ == "__main__":
    part1()
    part2()
