#!/usr/bin/env python
from dataclasses import dataclass


def read_input():
    with open('./inputs/day09') as f:
        return [l.strip() for l in f.readlines()]


@dataclass
class Knot:
    x: int
    y: int


def move_head(head, move):
    if move == 'U':
        head.y += 1
    elif move == 'D':
        head.y -= 1
    elif move == 'R':
        head.x += 1
    elif move == 'L':
        head.x -= 1


def move_tail(tail, head):
    if abs(head.x - tail.x) > 1:
        tail.x = (head.x + tail.x) // 2
        if head.x != tail.x:
            tail.y = head.y
    if abs(head.y - tail.y) > 1:
        tail.y = (head.y + tail.y) // 2
        if head.y != tail.y:
            tail.x = head.x


def part1():
    head, tail = Knot(0, 0), Knot(0, 0)
    visited = {(tail.x, tail.y)}

    for motion in read_input():
        move, steps = motion.split()
        steps = int(steps)

        while steps:
            move_head(head, move)
            move_tail(tail, head)
            visited.add((tail.x, tail.y))

            steps -= 1

    print(f'part 1: {len(visited)}')


if __name__ == '__main__':
    part1()
