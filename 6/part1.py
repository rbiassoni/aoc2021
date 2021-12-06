#! /usr/bin/python3.8
# -*- coding:utf8 -*-


"""
SPEC
input:  a number of days, a list of fishes
holding a status that is a is a 6 to 0 countdown
when a fish reaches 0 it spawns a new fisher with countdown set to 8
any further countdowns are 6 to like for founder fishes

output: number of fishes at the end of last day
"""


FIRST_COUNTDOWN_START = 8
COUNTDOWN_START = 6

ROUNDS = 256


def parse_input(fn):
    with open(fn) as f:
        return [int(n) for line in f.readlines() for n in line.strip().split(',')]


def run_sim(school, round_count=0):
    if round_count < ROUNDS:
        spawns = []
        for i, countdown in enumerate(school):
            if countdown:
                school[i] = countdown - 1
            else:
                school[i] = COUNTDOWN_START
                spawns.append(FIRST_COUNTDOWN_START)
        school += spawns
        round_count += 1
        run_sim(school, round_count=round_count)
    return len(school)


result = run_sim(parse_input("sample.txt"))
print(result)
