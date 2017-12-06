#!/usr/bin/env python

import sys

def solve1(file_name):

    with open(file_name) as f:
        rows = f.readlines()
        rows = [x.strip().split("\t") for x in rows] 

        row = [int(x) for x in rows[0]]

        tup_list = []
        tup = tuple(row)
        tup_list.append(tup)
        count = 0
        
        while(True):
            max_val = max(row)
            i_max = row.index(max_val)

            row[i_max] = 0
            for i in range(max_val):
                print((i_max + 1 + i) % (len(row) ))
                row[(i_max + 1 + i) % (len(row))] += 1
                print(row)

            count += 1
            tup = tuple(row)
            if tup in tup_list:
                break;
            else:
                tup_list.append(tup)
            



        print("output 1:")
        print(count)


def solve2(file_name):
    print("output 2:")
    	

if __name__ == "__main__":
    solve1(sys.argv[1])
    solve2(sys.argv[1])
