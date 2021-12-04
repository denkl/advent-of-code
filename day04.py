#!/usr/bin/env python
def read_input():
    with open('./inputs/day04') as f:
        nums = [int(n) for n in f.readline().strip().split(',')]

        boards = []
        lines = f.readlines()
        for s in range(0, len(lines), 6):
            board = [line.strip() for line in lines[s:s + 6]]
            board = [[int(i) for i in line.split()] for line in board if line]
            boards.append(board)

    return nums, boards


def score(board):
    rows, cols = [0] * 5, [0] * 5
    _score = 0
    for ri, row in enumerate(board):
        for ci, col in enumerate(row):
            if col is None:
                rows[ri] += 1
                cols[ci] += 1
                continue
            _score += col
    if 5 in rows or 5 in cols:
        return _score


def draw(board, num):
    for ri, row in enumerate(board):
        for ci, col in enumerate(row):
            if col != num:
                continue
            board[ri][ci] = None
            _score = score(board)
            return _score * num if _score else None


def part1():
    nums, boards = read_input()
    for num in nums:
        for board in boards:
            score = draw(board, num)
            if not score:
                continue
            print(f'part 1: {score}')
            return


if __name__ == '__main__':
    part1()
