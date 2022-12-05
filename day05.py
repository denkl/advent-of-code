#!/usr/bin/env python
from dataclasses import dataclass


def read_input():
    with open('./inputs/day05') as f:
        return [l.strip('\n') for l in f.readlines() if l.strip('\n')]


@dataclass
class Step:
    qty: int
    from_: int
    to: int


def stacks_and_steps():
    _stacks, steps = [], []
    for line in read_input():
        if line.startswith('move'):
            qty, from_, to = (
                int(i) for i in line.split() if i.isnumeric()
            )
            steps.append(
                Step(qty, from_ - 1, to - 1)
            )
        elif line.strip().startswith('['):
            _stacks.append(
                [line[i] for i in range(1, len(line), 4)]
            )

    stacks = [[] for _ in range(len(_stacks[0]))]
    for stack in reversed(_stacks):
        for i, crate in enumerate(stack):
            if crate.strip():
                stacks[i].append(crate)
    return stacks, steps



def part1():
    stacks, steps = stacks_and_steps()
    for step in steps:
        for _ in range(step.qty):
            stacks[step.to].append(
                stacks[step.from_].pop()
            )
    message = ''.join((s[-1] for s in stacks))
    print(f'part 1: {message}')


def part2():
    stacks, steps = stacks_and_steps()
    for step in steps:
        to_move = []
        for _ in range(step.qty):
            to_move.append(stacks[step.from_].pop())
        stacks[step.to].extend(reversed(to_move))
    message = ''.join((s[-1] for s in stacks))
    print(f'part 2: {message}')


if __name__ == '__main__':
    part1()
    part2()
