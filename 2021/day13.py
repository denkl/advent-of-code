#!/usr/bin/env python
def read_input():
    dots, folds = [], []
    with open("./inputs/day13") as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith("fold"):
                axis, val = line.split()[-1].split("=")
                iname = "ri" if axis == "y" else "ci"
                folds.append((iname, int(val)))
            elif line:
                ci, ri = [int(i) for i in line.split(",")]
                dots.append((ci, ri))
    return dots, folds


def part1():
    dots, folds = read_input()

    w, h = 0, 0
    for ci, ri in dots:
        h = max(h, ri)
        w = max(w, ci)

    paper = [[False] * (w + 1) for _ in range(h + 1)]
    for ci, ri in dots:
        paper[ri][ci] = True

    w, h = len(paper[0]), len(paper)
    for fold_count, fold in enumerate(folds):
        axis, fi = fold
        if axis == "ri":
            h = fi
            for ri, row in enumerate(paper[h:]):
                for ci, col in enumerate(row[:w]):
                    paper[h - ri][ci] = max(col, paper[h - ri][ci])
        elif axis == "ci":
            w = fi
            for ri, row in enumerate(paper[:h]):
                for ci, col in enumerate(row[w:]):
                    paper[ri][w - ci] = max(col, paper[ri][w - ci])

        if fold_count == 0:
            one_fold_dots = 0
            for row in paper[:h]:
                one_fold_dots += sum([i for i in row[:w] if i])

    print(f"part 1: {one_fold_dots}")
    print(f"part 2:")
    for row in paper[:h]:
        print("".join(["#" if i else "." for i in row[:w]]))


if __name__ == "__main__":
    part1()
