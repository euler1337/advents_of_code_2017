#!/usr/bin/env python

import sys

class ranked_stack:

    def __init__(self):
        self.values = []
        self.rank = 0
        self.count = 0

    def push(self):
        self.rank += 1
        self.values.append(self.rank)

    def pop(self):
        self.rank -= 1
        self.count += self.values.pop()

    def get_count(self):
        return self.count

def count_garbage(count, c, garbage):

    if(garbage):
        if c not in ['>', '!']:
            return count + 1
    return count 

def solve(file_name):

    with open(file_name) as f:
        rows = f.readlines()
        data_in = rows[0]

    group_stack = ranked_stack()

    # Detect start of group
    ignore = False
    garbage = False
    garbage_count = 0
    for c in data_in:

        if ignore == False :
            # Search for new groups
            garbage_count = count_garbage(garbage_count, c, garbage)

            if(garbage == False):
                if c == '{':
                    group_stack.push()
                elif c == '}':
                    group_stack.pop()
            if c == '!':
                ignore = True
            elif c == '<':
                garbage = True
            elif c == '>':
                garbage = False
        else:
            ignore = False
            continue

    print(group_stack.get_count())
    print(garbage_count)
            
if __name__ == "__main__":
    solve(sys.argv[1])
