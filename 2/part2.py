#! /usr/bin/python3.10
# -*- coding:utf8 -*-

with open("input.txt") as f:
    commands = f.readlines()

v = 0
h = 0
aim = 0

def move(command):
    global h, v, aim
    direction, units = command.split()
    # match case is brand new for python 3.10!
    match direction:
        case "forward":
            h += int(units)
            v += (int(units) * aim)
        case "up":
            aim -= int(units)
        case "down":
            aim += int(units)

moves = tuple(map(move, commands))
print(h*v)
