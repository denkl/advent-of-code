#!/usr/bin/env python
def read_input():
    with open('./inputs/day06') as f:
        return f.readline().strip()


def part1():
    stream = list(read_input())
    marker = 0
    for i, _ in enumerate(stream, 3):
        if len(set(stream[i-4:i])) == 4:
            marker = i
            break
    print(f'part 1: {marker}')


if __name__ == '__main__':
    part1()
