#!/usr/bin/env python
from collections import defaultdict
from dataclasses import dataclass
from itertools import zip_longest


@dataclass(frozen=True)
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    @property
    def points(self):
        rng = lambda p1, p2: range(min(p1, p2), max(p1, p2) + 1)
        return tuple(
            zip_longest(
                rng(self.x1, self.x2),
                rng(self.y1, self.y2),
                fillvalue=self.x1 if self.x1 == self.x2 else self.y1,
            )
        )


def read_input():
    with open("./inputs/day05") as f:
        return [
            Line(*(int(i) for i in line.replace(" -> ", ",").split(",")))
            for line in f.readlines()
        ]


def part1():
    lines = read_input()
    lines = [l for l in lines if l.x1 == l.x2 or l.y1 == l.y2]
    floor = defaultdict(int)
    for line in lines:
        for p in line.points:
            floor[(p[0], p[1])] += 1

    overlaps = len([v for v in floor.values() if v > 1])
    print(f"part 1: {overlaps}")


if __name__ == "__main__":
    part1()
