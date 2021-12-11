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
    sum of decoded outputs
"""
import string

UNIQ_PATTERN_LENGTHS = {2, 3, 4, 7}


CANONICAL_CODE = {
    'cf': 1,
    'acf': 7,
    'bcdf': 4,
    'acdeg': 2,
    'acdfg': 3,
    'abdfg': 5,
    'abcefg': 0,
    'abdefg': 6,
    'abcdfg': 9,
    'abcdefg': 8,
}


def parse_input(fn):
    with open(fn) as f:
        return (
            (
                ["".join(sorted(s)) for s in entry[0].strip().split(' ')],
                ["".join(sorted(s)) for s in entry[1].strip().split(' ')],
            )
            for line in f.readlines()
            # this is awkward and not very readable, but hey, walrus!
            if (entry := line.strip().split('|'))
        )


def get_known_local_code(sample):
    local_code = {}
    # TODO clean up this ugly thing
    # integers as keys are ugly
    # I should prolly reverse it even if access is difficult
    for s in sample:
        if len(s) == 2:
            local_code[1] = s
        elif len(s) == 3:
            local_code[7] = s
        elif len(s) == 4:
            local_code[4] = s
        elif len(s) == 7:
            local_code[8] = s
    return local_code


def decode_entry(sample, output):
    # this is based on geometric properties of the display kind
    # that make a number a subset of another
    # i really really do not like it
    # TODO explain and cleanup
    # don't do useless passes
    # pass 1
    local_code = get_known_local_code(sample)
    # pass 2
    for s in sorted(sample, key=len):
        if s not in local_code.values():
            if len(s) == 5:
                if set(local_code[1]) < set(s):
                    local_code[3] = s
            else:
                if set(local_code[3]) < set(s):
                    local_code[9] = s
                else:
                    if not (set(local_code[1]) < set(s)):
                        local_code[6] = s
                    else:
                        local_code[0] = s
    for s in sorted(sample, key=len):
        if s not in local_code.values():
            if len(s) == 5:
                if set(s) < set(local_code[9]):
                    local_code[5] = s
                else:
                    local_code[2] = s
    print(local_code)
    local_code = {v: k for k, v in local_code.items()}
    local_total = int(''.join([str(local_code[o]) for o in output]))
    return local_total


def decode(entries):
    return sum([decode_entry(entry[0], entry[1]) for entry in entries])


result = decode(parse_input("input.txt"))
print(result)
