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

from collections import Counter

FIRST_COUNTDOWN_START = 8
COUNTDOWN_START = 6
ROUNDS = 256


def parse_input(fn):
    with open(fn) as f:
        return Counter(
            [int(n) for line in f.readlines() for n in line.strip().split(',')]
        )


def run_sim(school, round_count=0):
    next_gen = Counter()
    if round_count < ROUNDS:
        for k, v in school.items():
            if k:
                next_gen[k - 1] = next_gen.get((k - 1), 0) + v
            else:
                next_gen[COUNTDOWN_START] = next_gen.get(COUNTDOWN_START, 0) + v
                next_gen[FIRST_COUNTDOWN_START] = v
        round_count += 1
        return run_sim(next_gen, round_count=round_count)
    return sum(school.values())


result = run_sim(parse_input("input.txt"))
print(result)
