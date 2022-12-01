#!/usr/bin/env python
from collections import defaultdict


def read_input():
    with open("./inputs/day10") as f:
        lines = f.readlines()
        return [s for line in lines for s in line if s != "\n"]


def is_closing(left, right):
    return left == {")": "(", "]": "[", "}": "{", ">": "<"}[right]


def part1():
    stack = []
    corrupted = defaultdict(int)
    for line in read_input():
        for s in line:
            if s in ("(", "[", "{", "<"):
                stack.append(s)
                continue

            opening = stack.pop()
            if not is_closing(opening, s):
                corrupted[s] += 1
                break

    score = sum(
        (
            corrupted[")"] * 3,
            corrupted["]"] * 57,
            corrupted["}"] * 1197,
            corrupted[">"] * 25137,
        )
    )
    print(f"part 1: {score}")


def part2():
    mapping = {"(": ")", "{": "}", "[": "]", "<": ">"}
    incomplete = []

    with open("./inputs/day10") as f:
        lines = [l.strip() for l in f.readlines()]

    for line in lines:
        stack = []
        for s in line:
            if s in ("(", "[", "{", "<"):
                stack.append(s)
                continue

            opening = stack.pop()
            if not is_closing(opening, s):
                stack = []
                break

        if stack:
            incomplete.append([mapping[s] for s in reversed(stack)])

    total_scores = []
    for line in incomplete:
        score = 0
        for s in line:
            score *= 5
            score += {")": 1, "]": 2, "}": 3, ">": 4}[s]
        total_scores.append(score)

    middle_score = sorted(total_scores)[len(total_scores) // 2]
    print(f"part 2: {middle_score}")


if __name__ == "__main__":
    part1()
    part2()
