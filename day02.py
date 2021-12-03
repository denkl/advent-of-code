#!/usr/bin/env python
def get_step():
    with open('./inputs/day02') as f:
        for step in f.readlines():
            cmd, v = step.split()
            yield cmd, int(v)


def part1():
    hp = depth = 0

    for cmd, v in get_step():
        match cmd:
            case 'forward':
                hp += v
            case 'down':
                depth += v
            case 'up':
                depth -= v

    print(f'part 1: {hp * depth}')


def part2():
    hp = aim = depth = 0

    for cmd, v in get_step():
        match cmd:
            case 'forward':
                hp += v
                if aim:
                    depth += aim * v
            case 'down':
                aim += v
            case 'up':
                aim -= v

    print(f'part 2: {hp * depth}')


if __name__ == '__main__':
    part1()
    part2()
