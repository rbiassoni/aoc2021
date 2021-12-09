#! /usr/bin/python3.10
# -*- coding:utf8 -*-


"""
SPEC
INPUT:
    a heightmap as a matrix of integers representing measurements
OUTPUT
   sum of risk level of low points in the matrix
   a low point is a point that is lower than all neighbors
   risk level is 1 + height  of point
"""


def parse_input(fn):
    with open(fn) as f:
        return [[int(c) for c in line.strip()] for line in f.readlines()]


def boundary_check(arr, row, col):
    if row >= 0 and row < len(arr) and col >= 0 and col < len(arr[0]):
        return arr[row][col]
    return None


def get_neighbors(radius, arr, row, col):
    row_neighbors = [
        v
        for ncol in range(col - radius, col + radius + 1, 2)
        if ((v := boundary_check(arr, row, ncol)) is not None)
    ]
    col_neighbors = [
        v
        for nrow in range(row - radius, row + radius + 1, 2)
        if ((v := boundary_check(arr, nrow, col)) is not None)
    ]
    return row_neighbors + col_neighbors


def get_lowpoints(arr):
    lowpoints = []
    for row, r in enumerate(arr):
        for col, v in enumerate(r):
            if all(v < n for n in get_neighbors(1, arr, row, col)):
                lowpoints.append(v + 1)
    return lowpoints


result = sum(get_lowpoints(parse_input("input.txt")))
print(result)
