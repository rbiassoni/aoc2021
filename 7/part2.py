#! /usr/bin/python3.8
# -*- coding:utf8 -*-


"""
SPEC
input:  a list of horizontal positions

find the position that implies the least moving from all these positions
every consecutive move implies + 1 move weight
output: total moves weight
"""


def parse_input(fn):
    with open(fn) as f:
        return [int(n) for line in f.readlines() for n in line.strip().split(',')]


def get_available_positions(arr):
    return range(min(arr), max(arr))


def get_move_totals(arr):
    move_totals = {}
    for x in get_available_positions(arr):
        move_total = 0
        for y in arr:
            move_total += sum([z for z in range(abs(x - y) + 1)])
        move_totals[x] = move_total
    return move_totals


def get_minimum_moves(totals):
    position = min(totals, key=totals.get)
    moves = totals[position]
    return position, moves


position, moves = get_minimum_moves(get_move_totals(parse_input("input.txt")))
print("{} moves at position {}".format(moves, position))
