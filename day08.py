#!/usr/bin/env python
from dataclasses import dataclass


segments = {
    0: "a b c e f g",
    1: "c f",
    2: "a c d e g",
    3: "a c d e f",
    4: "b c d f",
    5: "a b d f g",
    6: "a b d e f g",
    7: "a c f",
    8: "a b c d e f g",
    9: "a b c d f g",
}


@dataclass
class Entry:
    patterns: list[str]
    output: list[str]


def read_input():
    with open("./inputs/day08") as f:
        entries = []
        for line in f.readlines():
            patterns, output = line.strip().split(" | ")
            patterns = patterns.split()
            output = output.split()
            entries.append(Entry(patterns, output))
        return entries


def part1():
    entries = read_input()
    c = 0
    nums = [len(v.split()) for k, v in segments.items() if k in (1, 4, 7, 8)]
    for entry in entries:
        c += sum((1 for i in entry.output if len(i) in nums))
    print(f"part 1: {c}")


if __name__ == "__main__":
    part1()
