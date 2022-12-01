#!/usr/bin/env python
def get_measurements():
    with open('./inputs/day01') as f:
        return [int(v) for v in f.readlines()]


def part1():
    counter, prev = 0, float('inf')
    for v in get_measurements():
        if v > prev:
            counter += 1
        prev = v

    print(f'part 1: {counter}')


def part2():
    counter, prev = 0, float('inf')
    L = get_measurements()

    for i in range(len(L) - 2):
        curr = L[i] + L[i + 1] + L[i + 2]
        if curr > prev:
            counter += 1
        prev = curr

    print(f'part 2: {counter}')



if __name__ == '__main__':
    part1()
    part2()
