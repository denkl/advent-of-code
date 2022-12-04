#!/usr/bin/env python
def read_input():
    with open('./inputs/day04') as f:
        return [l.strip() for l in f.readlines()]


def _to_range(pair):
    return range(int(pair[0]), int(pair[1]) + 1)


def get_pairs():
    for line in read_input():
        yield (
            set(_to_range(p.split('-')))
            for p in line.split(',')
        )


def part1():
    total = 0
    for p1, p2 in get_pairs():
        if p1 >= p2 or p1 <= p2:
            total += 1
    print(f'part 1: {total}')


def part2():
    total = 0
    for p1, p2 in get_pairs():
        if p1 & p2:
            total += 1
    print(f'part 2: {total}')


if __name__ == '__main__':
    part1()
    part2()
