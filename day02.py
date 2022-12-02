#!/usr/bin/env python
def read_input():
    with open('./inputs/day02') as f:
        return f.readlines()


_map = {
    'A': 1,  # rock
    'X': 1,
    'B': 2,  # paper
    'Y': 2,
    'C': 3,  # scissors
    'Z': 3,
}


def play_round(opp, you):
    opp_v, you_v = _map[opp], _map[you]
    score = 0

    if opp_v == you_v:
        score = 3
    elif opp_v == 1:
        score = 6 if you_v == 2 else 0
    elif opp_v == 2:
        score = 0 if you_v == 1 else 6
    else:
        score = 6 if you_v == 1 else 0

    return score + you_v


def part1():
    total_score = sum(play_round(*v.strip().split()) for v in read_input())
    print(f'part 1: {total_score}')


if __name__ == '__main__':
    part1()
