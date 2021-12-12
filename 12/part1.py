#! /usr/bin/python3.10
# -*- coding:utf8 -*-


import string

from collections import defaultdict


def parse_input(fn):
    with open(fn) as f:
        segments = {tuple(line.strip().split('-')) for line in f.readlines()}
        reversibles = {
            (s[1], s[0])
            for s in segments
            if (s[0] not in ('start',) and s[1] not in ('end',))
        }
        segments |= reversibles
        return segments


# this is a modified depth first search
# see https://www.python.org/doc/essays/graphs/
def find_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or all([c in string.ascii_uppercase for c in node]):
            newpaths = find_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def get_graph(segments):
    graph = defaultdict(set)
    for a, b in segments:
        graph[a].add(b)
        graph[b].add(a)
    return graph


result = len(find_paths(get_graph(parse_input('input.txt')), 'start', 'end'))
print(result)
