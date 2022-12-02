#!/usr/bin/env python
def read_input():
    with open('./inputs/day02') as f:
        return f.readlines()


_map = {
    'A': 1,  # rock
    'B': 2,  # paper
    'C': 3,  # scissors
    'X': 1,
    'Y': 2,
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


def what_shape(opp, you):
    opp_v, you_v = _map[opp], _map[you]

    if you_v == 2:
        return {'A': 'X', 'B': 'Y', 'C': 'Z'}[opp]
    elif you_v == 1:  # lose
        return {1: 'Z', 2: 'X', 3: 'Y'}[opp_v]
    else:
        return {1: 'Y', 2: 'Z', 3: 'X'}[opp_v]



def part1():
    total_score = sum(play_round(*v.strip().split()) for v in read_input())
    print(f'part 1: {total_score}')


def part2():
    total_score = 0
    for v in read_input():
        opp, you = v.strip().split()
        total_score += play_round(opp, what_shape(opp, you))
    print(f'part 2: {total_score}')


if __name__ == '__main__':
    part1()
    part2()
