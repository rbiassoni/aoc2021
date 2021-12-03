#! /usr/bin/python3.10
# -*- coding:utf8 -*-


from collections import Counter

import BitVector

"""
SPEC
gamma = most common bit by position in bitstrings
epsilon = least common bit
power consumption = (base 10) gamma * epsilon
"""

with open("input.txt") as f:
    report = f.read().splitlines()


def get_most_common_bit_by_position(bitstrings):
    return BitVector.BitVector(
        bitstring=''.join(
            (
                Counter((bs[i] for bs in bitstrings)).most_common(1)[0][0]
                for i in range(len(report[0]))
            )
        )
    )


def get_int_invert_product(bits):
    return bits.int_val() * bits.__invert__().int_val()


power_consumption = get_int_invert_product(get_most_common_bit_by_position(report))
print(power_consumption)
