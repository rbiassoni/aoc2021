#! /usr/bin/python3.10
# -*- coding:utf8 -*-


import itertools


def parse_input(fn):
    with open(fn) as f:
        return [[int(c) for c in line.strip()] for line in f.readlines()]


def boundary_check(arr, row, col):
    if row >= 0 and row < len(arr) and col >= 0 and col < len(arr[0]):
        return (row, col)
    return None


def get_neighbors(radius, arr, row, col):
    return itertools.chain.from_iterable(
        [
            [
                v
                for j in range(col - radius, col + radius + 1)
                if ((v := boundary_check(arr, i, j)) is not None)
                and not (i == row and j == col)
            ]
            for i in range(row - radius, row + radius + 1)
        ]
    )


def mark_for_flash(arr, point, marked=set()):
    arr[point[0]][point[1]] = 0
    marked.add(point)
    neighbors = get_neighbors(1, arr, point[0], point[1])
    for n in neighbors:
        v = arr[n[0]][n[1]]
        if v == 0:
            continue
        else:
            arr[n[0]][n[1]] = v + 1
            if (v + 1) > 9:
                mark_for_flash(arr, n, marked=marked)
    return marked


def step(arr, marked):
    for row, r in enumerate(arr):
        for col, v in enumerate(r):
            arr[row][col] = v + 1
    for row, r in enumerate(arr):
        for col, v in enumerate(r):
            if (v) > 9:
                marked = mark_for_flash(arr, (row, col), marked=marked)
    return len(marked)


def main(arr, rounds):
    result = 0
    for r in range(rounds):
        marked = set()
        s = step(arr, marked)
        result += s
    return result


result = main(parse_input('input.txt'), 100)
print(result)
