#!/usr/bin/env python

import sys

def solve1(file_name):

    with open(file_name) as f:
    	rows = f.readlines()
    	rows = [x.strip().split("\t") for x in rows] 

    	delta = []
    	for row in rows:
    		r = [int(x) for x in row]
    		delta.append(max(r)-min(r))

    	print("output 1:")
    	print(sum(delta))


def solve2(file_name):
    with open(file_name) as f:
    	rows = f.readlines()
    	rows = [x.strip().split("\t") for x in rows] 

    	div = []
    	for row in rows:
    		r = [int(x) for x in row]
    		for digit in row:
    			digit = int(digit)

    			for index in range(len(row)):
    				other = int(row[index])

    				if(digit != other):
    					if(digit % other == 0):
    						div.append(digit/other)
    	print("output 2:")
    	print(sum(div))

if __name__ == "__main__":
    solve1(sys.argv[1])
    solve2(sys.argv[1])
