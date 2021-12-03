#!/usr/bin/env python
def part1():
    counter, prev = 0, float('inf')
    with open('./inputs/day01') as f:
        for v in f.readlines():
            v = int(v)
            if v > prev:
                counter += 1
            prev = v

    print(f'part 1: {counter}')



if __name__ == '__main__':
    part1()
