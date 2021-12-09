#! /usr/bin/python3.10
# -*- coding:utf8 -*-


"""
SPEC
INPUT:
    a heightmap as a matrix of integers representing measurements
OUTPUT
   product of three largest basin sizes
   a basin is composed of adjacent cells, not including 9 valued cells
   that grade into a lowerpoint
   a low point is a point that is lower than all neighbors
"""

import math


def parse_input(fn):
    with open(fn) as f:
        return [[int(c) for c in line.strip()] for line in f.readlines()]


def boundary_check(arr, row, col):
    if row >= 0 and row < len(arr) and col >= 0 and col < len(arr[0]):
        return arr[row][col]
    return None


def get_neighbors(radius, arr, row, col):
    row_neighbors = [
        (row, ncol, v)
        for ncol in range(col - radius, col + radius + 1, 2)
        if ((v := boundary_check(arr, row, ncol)) is not None)
    ]
    col_neighbors = [
        (nrow, col, v)
        for nrow in range(row - radius, row + radius + 1, 2)
        if ((v := boundary_check(arr, nrow, col)) is not None)
    ]
    return row_neighbors + col_neighbors


def get_lowpoints(arr):
    lowpoints = []
    for row, r in enumerate(arr):
        for col, v in enumerate(r):
            if all(v < n[2] for n in get_neighbors(1, arr, row, col)):
                lowpoints.append((row, col, v))
    return lowpoints


def in_basin(point, lowpoint):
    in_basin = (point[2] != 9) and (point[2] > lowpoint[2])
    return in_basin


def get_basin(arr, lowpoint, basin=set(), round=0):
    if round == 0:
        basin = {lowpoint}
    neighbors = get_neighbors(1, arr, lowpoint[0], lowpoint[1])
    for n in neighbors:
        if in_basin(n, lowpoint) and not (n in basin):
            basin.add(n)
            round += 1
            get_basin(arr, n, basin=basin, round=round)
    return basin


def main(arr):
    lowpoints = get_lowpoints(arr)
    basins = [get_basin(arr, lowpoint) for lowpoint in lowpoints]
    relevant_basin_sizes = list(sorted([len(basin) for basin in basins]))[-3:]
    return math.prod(relevant_basin_sizes)


result = main(parse_input("input.txt"))
print(result)
