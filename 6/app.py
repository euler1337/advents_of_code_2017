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
                row[(i_max + 1 + i) % (len(row))] += 1

            count += 1
            tup = tuple(row)
            if tup in tup_list:
                first_occurance_index = tup_list.index(tup)
                loop_length = len(tup_list) - first_occurance_index
                break;
            else:
                tup_list.append(tup)




        print("output 1:")
        print(count)
        print("output 2:")
        print(loop_length)




if __name__ == "__main__":
    solve1(sys.argv[1])
