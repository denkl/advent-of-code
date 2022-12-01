#!/usr/bin/env python
from functools import lru_cache


def read_input():
    with open("./inputs/day06") as f:
        return [int(i) for i in f.readline().strip().split(",")]


def part1():
    ages = read_input()
    days = 80
    while days > 0:
        new = 0
        for i, age in enumerate(ages):
            if age == 0:
                ages[i] = 6
                new += 1
            else:
                ages[i] -= 1
        ages.extend([8] * new)
        days -= 1

    print(f"part 1: {len(ages)}")


@lru_cache
def descedants_num(timer, days):
    num = 0
    birthdays = grow(timer, days)
    num += len(birthdays)
    for day in birthdays:
        num += descedants_num(8, day - 1)
    return num


@lru_cache
def grow(timer, days_count):
    birthdays = []
    while days_count > 0:
        if timer == 0:
            timer = 6
            birthdays.append(days_count)
        else:
            timer -= 1
        days_count -= 1
    return birthdays


def part2():
    num = sum((descedants_num(t, 256) + 1 for t in read_input()))
    print(f"part 2: {num}")


if __name__ == "__main__":
    part1()
    part2()
