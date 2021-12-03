#! /usr/bin/python3.10
# -*- coding:utf8 -*-


from collections import Counter
from functools import partial
from itertools import tee

"""
SPEC
The bit criteria depends on which type of rating value you want to find:
    To find oxygen generator rating, determine the most common value (0 or 1) in the
    current bit position, and keep only numbers with that bit in that position.
    If 0 and 1 are equally common, keep values with a 1 in the position considered.
    To find CO2 scrubber rating, determine the least common value (0 or 1)
    in the current bit position, and keep only numbers with that bit in that position.
    If 0 and 1 are equally common, keep values with a 0 in the position considered.

Keep only numbers selected by the bit criteria for the type of rating value for which
you are searching. Discard numbers which do not match the bit criteria.
If you only have one number left, stop; this is the rating value for which you are
searching. Otherwise, repeat the process, considering the next bit to the right.
"""

with open("input.txt") as f:
    report = f.read().splitlines()

ROUNDUP_METRICS = ("oxigen",)


def get_check(counter, target):
    if counter.most_common()[0][1] != counter.most_common()[1][1]:
        check = (
            counter.most_common()[0][0]
            if target in ROUNDUP_METRICS
            else counter.most_common()[1][0]
        )
    else:
        check = "1" if target in ROUNDUP_METRICS else "0"
    return check


def selector(position, check, bitstring):
    return bitstring[position] == check


def select_metric(bitstrings, metric, position=0):
    it = iter(bitstrings)
    wc_1, wc_2 = tee(it)
    try:
        counter = Counter((bs[position] for bs in wc_1))
        check = get_check(counter, metric)
    except IndexError:
        return int(tuple(wc_2)[0], 2)
    bitstrings_subset = filter(partial(selector, position, check), wc_2)
    position += 1
    return select_metric(bitstrings_subset, metric, position=position)


print(select_metric(report, "oxigen") * select_metric(report, "scrubber"))
