#!/usr/bin/env python
def read_input():
    with open('./inputs/day06') as f:
        return f.readline().strip()


def find_marker(length):
    stream = list(read_input())
    for i, _ in enumerate(stream, length-1):
        if len(set(stream[i-length:i])) == length:
            return i


def part1():
    marker = find_marker(4)
    print(f'part 1: {marker}')


def part2():
    marker = find_marker(14)
    print(f'part 2: {marker}')


if __name__ == '__main__':
    part1()
    part2()
