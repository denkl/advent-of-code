#!/usr/bin/env python
from pathlib import Path
from collections import defaultdict


def read_input():
    with open('./inputs/day07') as f:
        return [l.strip() for l in f.readlines()]


def dirs_table():
    ftable, dtable = defaultdict(int), defaultdict(int)
    cwd = Path('/')
    dtable[cwd]

    for line in read_input():
        if line.startswith('$ cd'):
            target = line.split()[-1]
            if target == '..':
                cwd = cwd.parent
            else:
                cwd = cwd / target

        elif line.startswith('$ ls'):
            continue

        elif line.startswith('dir'):
            name = line.split()[-1]
            dtable[cwd / name]

        else:
            size, name = line.split()
            ftable[cwd / name] = int(size)

    for dir_ in dtable:
        files = {
            file: size for file, size in ftable.items()
            if dir_ in file.parents
        }
        dtable[dir_] = sum(files.values())

    return dtable



def part1():
    total = sum((s for s in dirs_table().values() if s <= 100000))
    print(f'part 1: {total}')


def part2():
    dtable = dirs_table()
    to_free = 30000000 - (70000000 - dtable[Path('/')])
    smallest = min((s for s in dtable.values() if s >= to_free))
    print(f'part 2: {smallest}')


if __name__ == '__main__':
    part1()
    part2()

