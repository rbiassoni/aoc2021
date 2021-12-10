#! /usr/bin/python3.10
# -*- coding:utf8 -*-


"""
SPEC
a parser, finally
INPUT:
    Several lines containing chunks.
    There are one or more chunks on each line,
    and chunks contain zero or more other chunks.
    Adjacent chunks are not separated by any delimiter.
    Every chunk must open and close with one of four legal pairs of matching characters:
    (, [, {, < etc
OUTPUT
   Corrupted lines
   A corrupted line is one where a chunk closes with the wrong character
   Take the first illegal character on the line
   Use the scoring table.
"""

SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
OPENERS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
CLOSERS = {v: k for k, v in OPENERS.items()}


def parse_input(fn):
    with open(fn) as f:
        return f.readlines()


def syntax_check(line):
    opens = []
    for c in line.strip():
        if c in OPENERS:
            opens.append(c)
        else:
            if CLOSERS[c] == opens[-1]:
                opens.pop()
            else:
                return c


def main(lines):
    score = sum([SCORES[error] for line in lines if (error := syntax_check(line))])
    return score


result = main(parse_input('input.txt'))
print(result)
