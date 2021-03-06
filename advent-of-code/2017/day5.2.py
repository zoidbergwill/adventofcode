#!/usr/bin/env python3
import fileinput
from collections import *
from functools import *
from itertools import *
from math import *


def process(lines):
    pointer = 0
    moves = 0
    while 0 <= pointer < len(lines):
        move = lines[pointer]
        if lines[pointer] >= 3:
            lines[pointer] -= 1
        else:
            lines[pointer] += 1
        pointer += move
        moves += 1
    return moves

lines = []
for line in fileinput.input():
    line = line.strip()
    lines.append(int(line))


print('{} moves taken until exit'.format(process(lines)))
