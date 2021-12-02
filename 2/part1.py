#! /usr/bin/python3.10
# -*- coding:utf8 -*-

with open("input.txt") as f:
    commands = f.readlines()

h = 0
v = 0

def move(command):
    global h, v
    direction, units = command.split()
    # match case is brand new for python 3.10!
    match direction:
        case "forward":
            h += int(units)
        case "up":
            v -= int(units)
        case "down":
            v += int(units)

moves = tuple(map(move, commands))
print(h*v)
