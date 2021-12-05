#! /usr/bin/python3.8
# -*- coding:utf8 -*-


"""
SPEC
input: a list coordinate pairs
output: count of intersections between segments joining each pair
of vertical or horizontal lines
"""

from collections import Counter

# Implementation of https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
# which is an error corrected version of
# https://en.wikipedia.org/wiki/Digital_differential_analyzer_(graphics_algorithm)

from bresenham import bresenham


def parse_data(fn):
    with open(fn) as f:
        coordinates = (
            [int(x) for tup in line.strip().split(' -> ') for x in tup.split(',')]
            for line in f.readlines()
        )
    return filter(is_axial, coordinates)


def is_axial(segment):
    x0, y0, x1, y1 = segment
    return (x0 == x1) or (y0 == y1)


def get_segment_coordinates(coordinates):
    return (p for coordinates_pair in coordinates for p in bresenham(*coordinates_pair))


def get_intersection_count(segment_coordinates):
    return sum(
        [1 for coordinate, count in Counter(segment_coordinates).items() if count > 1]
    )


result = get_intersection_count(get_segment_coordinates(parse_data("input.txt")))
print(result)
