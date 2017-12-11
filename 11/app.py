#!/usr/bin/env python

import sys
import math

def solve(file_name):

    coords = {'s' : 0, 'sw' : 0, 'se' : 0}

    with open(file_name) as f:
        rows = f.readlines()
        data_in = rows[0]

    max_dist = 0
    for c in [x.strip() for x in data_in.split(",")]:
        if c == 'n':
            coords['s'] -= 1
        elif c == 's':
            coords['s'] += 1
        elif c == 'ne':
            coords['sw'] -= 1
        elif c == 'sw':
            coords['sw'] += 1
        elif c == 'nw':
            coords['se'] -= 1
        elif c == 'se':
            coords['se'] += 1
        else:
            Raise(IOError("invalid input."))

        vertical = math.ceil(coords['s'] + (coords['se'] + coords['sw'])/2)
        diagonal = coords['se'] - coords['sw']

        vertical_tolerance = math.floor(diagonal/2)
        
        distance = diagonal + max(abs(vertical) - vertical_tolerance,0)
        max_dist = max(max_dist, distance)

    print(distance)
    print(max_dist)

            
if __name__ == "__main__":
    solve(sys.argv[1])
