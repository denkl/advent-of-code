#!/usr/bin/env python
from pathlib import Path
from collections import defaultdict


def read_input():
    with open('./inputs/day07') as f:
        return [l.strip() for l in f.readlines()]


def dirs_table():
    ftable, dtable = defaultdict(int), defaultdict(int)
    cwd = Path('/')

    for line in read_input():
        if line.startswith('$ cd'):
            target = line.split()[-1]
            if target == '/':
                continue
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
    total = 0
    for size in dirs_table().values():
        if size <= 100000:
            total += size
    print(f'part 1: {total}')


if __name__ == '__main__':
    part1()

