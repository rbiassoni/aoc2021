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
   Incomplete lines
   An incomplete line is missing some characters at the end of the line
   Get the closing sequence
   Use the scoring table like this
   start at 0
   for each char multiply by 5, add accoridng to scoring table
   sort per line results
   take the middle one
"""

SCORES = {')': 1, ']': 2, '}': 3, '>': 4}
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
                return []
    return opens


def score(closing_sequence):
    s = SCORES[closing_sequence[0]]
    for c in closing_sequence[1:]:
        s = (s * 5) + SCORES[c]
    return s


def main(lines):
    closing_sequences = [
        [OPENERS[c] for c in list(reversed(line_opens))]
        for line in lines
        if (line_opens := syntax_check(line))
    ]
    scores = [score(closing_sequence) for closing_sequence in closing_sequences]
    middle_score = sorted(scores)[len(scores) // 2]
    return middle_score


result = main(parse_input('input.txt'))
print(result)
