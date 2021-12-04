#! /usr/bin/python3.10
# -*- coding:utf8 -*-


"""
SPEC
input: a list of numbers
+
a set of bingo boards

the first board in which all numbers in a row or column appear wins
return its score, calculated as the sum of all uncalled numbers
multiplied by the lst called one
"""
from io import StringIO

import numpy as np


def parse_bingo(game):
    draws = game.pop(0).split(",")
    boards = [np.loadtxt(StringIO(board), dtype=int) for board in game]
    board_size = boards[0].shape[0]
    return draws, boards, board_size


def score(draw, board):
    return int(np.nansum(board)) * int(draw)


def is_winner(board, size):
    for i in range(size):
        drawn_row = np.sum(np.isnan(board[i, :]))
        drawn_col = np.sum(np.isnan(board[:, i]))
        if size in (drawn_row, drawn_col):
            return True
    return False


def find_winner(draws, boards, board_size):
    for count_draw, draw in enumerate(draws):
        for count_board, board in enumerate(boards):
            board = np.where(board == int(draw), np.nan, board)
            boards[count_board] = board
            if count_draw >= board_size:
                if is_winner(board, board_size):
                    return draw, board


with open("input.txt") as f:
    game = f.read().split('\n\n')
    draws, boards, board_size = parse_bingo(game)
    draw, winner = find_winner(draws, boards, board_size)
    print(draw)
    print(winner)
    score = score(draw, winner)
    print(score)
