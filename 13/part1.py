#! /usr/bin/python3.10
# -*- coding:utf8 -*-

import numpy as np


def parse_input(fn):
    with open(fn) as f:
        dots = []
        folds = []
        for line in f.readlines():
            if line.startswith('fold'):
                print(line)
                fold_axis = line.split('=')[0][-1]
                fold_line = line.split('=')[1][0]
                folds.append((fold_axis, fold_line))
            else:
                dot = line.strip().split(',')
                if len(dot) == 2:
                    dots.append(tuple(dot))
        rows = max([int(dot[1]) for dot in dots]) + 1
        cols = max([int(dot[0]) for dot in dots]) + 1
        arr = np.zeros((rows, cols), dtype=int)
        return dots, folds, arr


def populate(arr, dots):
    for dot in dots:
        arr[int(dot[1])][int(dot[0])] = 1
    return arr


def fold(arr, foldspec):
    axis = 1 if foldspec[0] == 'x' else 0
    subarr = np.array_split(arr, [int(foldspec[1])], axis)
    secondary = np.flip(subarr[1][1:], axis)
    print(secondary)
    # either find a numpy way to do it (masked arrays?)
    # por caluclate where 1s will be applied
    # and change if necessary
    # numpy concatenate at the correct point
    # ( its a mask, not a simple merge)
    return arr


def count_dots(arr):
    return np.count_nonzero(arr)


def main():
    dots, folds, arr = parse_input('sample.txt')
    arr = fold(populate(arr, dots), folds[0])
    # print(arr)
    count = count_dots(arr)
    print(count)


# print(result)
main()
