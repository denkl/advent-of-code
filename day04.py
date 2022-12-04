#!/usr/bin/env python
def read_input():
    with open('./inputs/day04') as f:
        return [l.strip() for l in f.readlines()]


def _to_range(pair):
    return range(int(pair[0]), int(pair[1]) + 1)


def part1():
    total = 0
    for line in read_input():
        pair1, pair2 = [
            set(_to_range(p.split('-')))
            for p in line.split(',')
        ]
        if pair1 >= pair2 or pair1 <= pair2:
            total += 1
    print(f'part 1: {total}')


if __name__ == '__main__':
    part1()
