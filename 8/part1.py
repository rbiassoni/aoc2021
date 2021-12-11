#! /usr/bin/python3.8
# -*- coding:utf8 -*-


"""
SPEC
4 digit, 7 segment displays
segments are named a, b, c...

0 = abcefg
1 = cf
2 = acdeg
3 = acdfg
4 = bcdf
5 = abdfg
6 = abdefg
7 = acf
8 = abcdefg
9 = abcdfg

1, 4, 7, and 8 are uniq in len
the theme is (involuntary) cryptography

signal is mismatched e.g. input g turns on segment b
the randomisation of signal is per display

INPUT:
    lines like

    "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
    cdfeb fcadb cdfeb cdbaf"

    - ten signal patterns, a sample of ten digits rendered in the specifically
    botched way of that display
    - a separator '|'
    - the four digits that we actually want to decode and output, botched the same way
OUTPUT
    how many times digits with a unique number of segments (1, 4, 7, 8)
    appear in outputs
"""

UNIQ_PATTERN_LENGTHS = {2, 3, 4, 7}


def parse_input(fn):
    with open(fn) as f:
        return (
            (entry[0].strip().split(' '), entry[1].strip().split(' '))
            for line in f.readlines()
            # this is awkward and not very readable, but hey, walrus!
            if (entry := line.strip().split('|'))
        )


def get_uniq_patterns_count(entries):
    count = 0
    for entry in entries:
        for value in entry[1]:
            if len(value) in UNIQ_PATTERN_LENGTHS:
                count += 1
    return count


result = get_uniq_patterns_count(parse_input("input.txt"))
print(result)
